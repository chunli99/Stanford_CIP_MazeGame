import sys
print("Python version")
print(sys.version)

import pkg_resources
print("Installed packages")
installed_packages = pkg_resources.working_set
for package in installed_packages:
    print(package.project_name, package.version)