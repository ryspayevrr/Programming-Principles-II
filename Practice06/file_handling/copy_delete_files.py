import shutil
import os


print(os.getcwd())

shutil.copy("sample.txt", "backup.txt")

if os.path.exists("backup.txt"):
    os.remove("backup.txt")