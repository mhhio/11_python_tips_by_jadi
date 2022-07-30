'''
cross platform path library
'''
from pathlib import Path

# home
print(Path.home())
# list files and print absolute paths
current_path = Path()
print(current_path.absolute())
for python_file in current_path.glob("*.py"):
    print(python_file.absolute())
