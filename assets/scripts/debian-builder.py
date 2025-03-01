#!/usr/bin/env python3
import argparse
import os
import sys

VERSION = "1.0.0"

class Package:
    def __init__(self, path, package_name):
        self.path = path
        self.package_name = package_name
        self.py_file_path = ""

    def build(self):
        deb_file = f"{self.path}.deb"
        if self.verify_deb_exists(deb_file):
            print(f"Package {deb_file} already exists!")
            return
        
        print(f'\nBuilding package {self.package_name}')
        os.system(f'sudo dpkg-deb --build {self.path}')
        print('Package built successfully')

    def verify_deb_exists(self, package_path):
        if os.path.isfile(package_path):
            return True
        return False

    def remove_deb_file(self):
        os.system(f'rm -f {self.path}.deb')

    def convert_py_file(self, py_file_path):
        if not os.path.isfile(py_file_path):
            print('.py file not found')
            exit(0)

        if not py_file_path:
            print("\nPlease provide the .py file path with -p or --path")
            exit(0)

        print("\nCopying file and removing .py extension...")
        self.py_file_path = py_file_path
        new_path = self.py_file_path.replace('.py', '')
        os.system(f"sudo cp {self.py_file_path} {new_path}")
        print(f"Process executed successfully!")

    def permission_to_execute(self):
        if not self.py_file_path:
            print("\nError: Python file path not set. Did you run the conversion step?")
            return
        
        print(f'\nGiving {self.py_file_path.split("/")[-1].replace(".py", "")} execution permission...')
        converted_py_file_path = f'{self.py_file_path.replace(".py", "")}'
        os.system(f'sudo chmod +x {converted_py_file_path}')
        print(f'Permission given successfully!')

    def uninstall_deb_package(self):
        print(f'\nRemoving {self.package_name} package...')
        os.system(f"sudo dpkg -r {self.package_name}")
        os.system(f"sudo dpkg --purge {self.package_name}")
        os.system(f"sudo apt autoremove")
        print(f"{self.package_name} removed successfully!")

    def install_deb_package(self):
        self.convert_py_file(f"{self.path}/usr/bin/{self.package_name}.py")
        self.permission_to_execute()
        print(f'\nInstalling package: {self.package_name}...')
        os.system(f'sudo dpkg -i {self.path}.deb')
        print(f'Package installed successfully!')

def main():
    parser = argparse.ArgumentParser(description="Debian builder is a tool created to facilitate the building process of debian packages")

    parser.add_argument('-b', '--build', action="store_true", help="Build debian package")
    parser.add_argument('-p', '--path', type=str, help="Package folder directory")
    parser.add_argument('-n', '--name', type=str, help="Package name")
    parser.add_argument('--reinstall', action='store_true', help="Active this option if you want to uninstall and install the package again")
    parser.add_argument('-u', '--uninstall', action='store_true', help='To uninstall a package')
    parser.add_argument('-f', '--fullbuild', action='store_true', help='Will basically remove .deb package, convert .py file, uninstall package, create a new .deb package and install it')
    parser.add_argument('-c', '--convert', action='store_true', help='Convert any file into a executable file')

    try:
        args = parser.parse_args()
    except:
        print("Error: command line option values unexpected")
        sys.exit(3)

    if args.convert and args.path:
        py_file = Package(args.path, '')
        py_file.convert_py_file(f'{py_file.path}')
        py_file.permission_to_execute()

    if args.build:
        if args.path and args.name:
            package = Package(args.path, args.name)
            package.build()
        else:
            print("You need to specify the package folder directory with --path or -p and the package name with --name")

    if args.fullbuild and args.path and args.name:
        package = Package(args.path, args.name)
        if package.verify_deb_exists(f"{args.path}.deb"):
            package.remove_deb_file()
        package.convert_py_file(f"{package.path}/usr/bin/{package.package_name}.py")
        package.permission_to_execute()
        package.uninstall_deb_package()
        package.build()
        package.install_deb_package()

    if args.uninstall and args.name:
        package_to_remove = Package("", args.name)
        package_to_remove.uninstall_deb_package()

    if args.reinstall:
        if args.path and args.name:
            package = Package(args.path, args.name)
            package.uninstall_deb_package()
            package.install_deb_package()
        else:
            print("You need to specify the package folder directory with --path or -p and the package name with --name")

if __name__ == "__main__":
    main()
