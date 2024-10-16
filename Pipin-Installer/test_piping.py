import subprocess
import os
from pipin import install_requirements

# List of libraries to test with
TEST_LIBRARIES = [
    'requests==2.26.0',
    'numpy==1.21.2',
    'pandas==1.3.3',
    'scipy==1.7.1',
    'matplotlib==3.4.3',
    'scikit-learn==0.24.2',
    'beautifulsoup4==4.10.0',
    'lxml==4.6.3',
    'flask==2.0.1',
    'SQLAlchemy==1.4.23',
    'pytest==6.2.4',
    'seaborn==0.11.2',
    'Jinja2==3.0.1'
]


# Step 1: Create a temporary requirements.txt file for testing
def create_test_requirements():
    print("Creating test 'requirements.txt' file with the following libraries:")
    for lib in TEST_LIBRARIES:
        print(f"  - {lib}")
    
    with open('requirements.txt', 'w') as req_file:
        req_file.writelines([lib + '\n' for lib in TEST_LIBRARIES])

# Step 2: Test installation of libraries using the piping script
def test_installation():
    print("\nStarting installation of test libraries using pipin.py...")
    install_requirements()  # Call the function from pipin.py to install packages

    # Check if libraries were installed
    for lib in TEST_LIBRARIES:
        package_name = lib.split('==')[0]
        result = subprocess.run(['pip', 'show', package_name], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  - {package_name} is installed.")
        else:
            print(f"  - {package_name} installation failed.")

# Step 3: Uninstall the test libraries after installation
def uninstall_test_libraries():
    print("\nUninstalling test libraries...")
    for lib in TEST_LIBRARIES:
        package_name = lib.split('==')[0]
        result = subprocess.run(['pip', 'uninstall', '-y', package_name], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  - {package_name} uninstalled successfully.")
        else:
            print(f"  - {package_name} uninstallation failed or it wasn't installed.")

# Step 4: Clean up the temporary 'requirements.txt' file
def clean_up():
    if os.path.exists('requirements.txt'):
        os.remove('requirements.txt')
        print("\nCleaned up 'requirements.txt'.")

# Main test runner
if __name__ == "__main__":
    create_test_requirements()    # Step 1: Create test requirements file
    test_installation()           # Step 2: Test installation of libraries
    uninstall_test_libraries()    # Step 3: Uninstall the libraries
    clean_up()                    # Step 4: Clean up
