# understanding files
with open("file.txt", "r") as f:
    f_contents = f.readline()
    print(f_contents)
    print(f.tell())
