import os
import shutil

path = str(input("Path: "))
os.chdir(path)
files = os.listdir()

for file in files:
    name, ext = os.path.splitext(file)

    if os.path.exists(path + '/' + ext):
        shutil.move(file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(file, path + '/' + ext + '/' + file)

print("Success")