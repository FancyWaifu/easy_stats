import subprocess
import sys

# List of packages to install
packages = [
    'statistics',
    'numpy',
    'pandas',
]

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

if __name__ == '__main__':
    for package in packages:
        try:
            install(package)
            print(f'Successfully installed {package}')
        except subprocess.CalledProcessError as e:
            print(f'Failed to install {package}. Error: {e}')
