import os

files = []

for file in os.listdir():
    if file.endswith(".py"):
        continue

    if os.path.isdir(file):
        continue

    files.append(file)

