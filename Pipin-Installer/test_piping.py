import subprocess
import shutil
import os
from pipin import install_requirements

# Full test libraries list with various scenarios: valid, invalid, conflicting, etc.
TEST_LIBRARIES = [
    'requests==2.26.0',  # Valid version
    'numpy==1.21.2',  # Valid version
    'tensorflow==2.0.0',  # Potential conflict with numpy
    'beautifulsoup4==4.10.0',  # Valid
    'lxml==4.6.3',  # Valid
    'flask==2.0.1',  # Valid
    'SQLAlchemy==1.4.23',  # Valid
    'pytest==6.2.4',  # Valid
    'Jinja2==3.0.1',  # Valid
    'Django==3.2',  # Valid
    'Django==2.2',  # Conflicting version of Django
    'pandas==1.3.3',  # Valid
    'matplotlib==3.4.3'  # Valid
]


# Create a test requirements.txt file for testing purposes
def create_test_requirements():
    """Creates a requirements.txt file with the test libraries."""
    with open('requirements.txt', 'w') as req_file:
        req_file.write('\n'.join(TEST_LIBRARIES))

# Uninstall all test libraries to clean up the environment
def uninstall_libraries():
    """Uninstalls all libraries listed in the TEST_LIBRARIES."""
    print("\nUninstalling all test libraries...")
    for lib in TEST_LIBRARIES:
        lib_name = lib.split('==')[0]
        subprocess.run(['pip', 'uninstall', lib_name, '-y'])
    print("Uninstallation complete.")

# Run the full set of installation and logging tests
def run_installation_test():
    print("Starting installation tests...")

    # 1. Test with valid and invalid versions
    print("\nCreating and installing from test requirements.txt (valid + invalid versions)...")
    create_test_requirements()
    install_requirements()

    # 2. Test with omitting specific libraries
    print("\nTesting omitting libraries during installation...")
    omit_libraries = ['requests']
    install_requirements(omit_libraries=omit_libraries)

    # 3. Test with missing requirements.txt
    print("\nSimulating a missing requirements.txt file...")
    shutil.move('requirements.txt', 'requirements_backup.txt')
    install_requirements()  # Should handle the missing file case and log an error
    shutil.move('requirements_backup.txt', 'requirements.txt')

    # 4. Test with an empty requirements.txt
    print("\nSimulating an empty requirements.txt file...")
    with open('requirements.txt', 'w') as empty_file:
        empty_file.write('')
    install_requirements()  # Should handle empty file case gracefully

    # 5. Test conflicting versions (already part of TEST_LIBRARIES)

    # 6. Manual Test: Simulate network issues by disabling the internet (uncomment to try)
    # print("\nSimulating network issues (disable internet manually for this test)...")
    # subprocess.run(['sudo', 'ifconfig', 'eth0', 'down'])
    # install_requirements()
    # subprocess.run(['sudo', 'ifconfig', 'eth0', 'up'])

    # 7. Uninstall all test libraries
    uninstall_libraries()

    print("\nAll tests completed.")

if __name__ == "__main__":
    run_installation_test()
