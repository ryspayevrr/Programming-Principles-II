with open("sample.txt", "w") as f:
    f.write("Musketeer Mortar Valkyrie\n")


with open("sample.txt", "a") as f:
    f.write("Crow Spike Sirius")


# with automatically closes the file, no need for close()