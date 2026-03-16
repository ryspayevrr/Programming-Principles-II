import os

os.mkdir("test_folder")

os.makedirs("parent/child/grandchild")

files = os.listdir(".")

print(files)

print("\n")


for f in files:
    if f.endswith(".txt"):
        print(f)

os.chdir("test_folder")