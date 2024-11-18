#------------------------------------------------------------------------------------
# Developed by MalkasianGroup, LLC.
#------------------------------------------------------------------------------------
# Legal Notice: Distribution Authorized. GNU General Public License (GPL)
#------------------------------------------------------------------------------------

#------------------------------------NOTES-------------------------------------------

# ADD THIS TO YOUR CODE:
# add_version(CURRENT_VERSION, CHANGES)
# server_version = get_latest_version()

#-----------------------------------IMPORTS------------------------------------------
import os


#----------------------------------CONST VARS----------------------------------------

CHANGELOG_FILE = "CHANGELOG.txt"

#------------------------------------FUNCTIONS---------------------------------------
def initialize_changelog():
    """Ensure the changelog file exists; create if not."""
    if not os.path.exists(CHANGELOG_FILE):
        with open(CHANGELOG_FILE, "w") as file:
            file.write("#------------------------------------CHANGE LOG---------------------------------------\n")
        print(f"{CHANGELOG_FILE} created.")
    else:
        print(f"{CHANGELOG_FILE} already exists.")

def get_latest_version():
    """Retrieve the latest version from the changelog."""
    if not os.path.exists(CHANGELOG_FILE):
        return None

    with open(CHANGELOG_FILE, "r") as file:
        for line in reversed(file.readlines()):
            if line.strip().startswith("# Version"):
                return line.split()[2].strip()  # Extract the version number
    return None

def add_version(version, changes):
    """Add a new version to the changelog or skip if it already exists."""
    initialize_changelog()

    with open(CHANGELOG_FILE, "r") as file:
        lines = file.readlines()
        existing_versions = [line.split()[2] for line in lines if line.strip().startswith("# Version")]

    if version in existing_versions:
        print(f"Version {version} already exists. No updates made.")
        return version

    # Append the new version and changes
    with open(CHANGELOG_FILE, "a") as file:
        file.write(f"# Version {version} - {changes}\n")
    print(f"Version {version} added to the changelog.")
    return version


def get_server_info():
    """Display server version and environment details."""
    server_version = get_latest_version() or "No version found"
    print("========================================")
    print(f"Server Version: {server_version}")
    print("========================================")
