import os
import hashlib
import json

def hashFile(filep):
    sha = hashlib.sha256()

    try:
        file = open(filep, "rb")
        data = file.read()
        file.close()

        sha.update(data)
        return sha.hexdigest()

    except:
        return None


def traverseDirectory(directroy):
    hash_table = {}

    try:
        files = os.listdir(directroy)

        for name in files:
            path = os.path.join(directroy, name)

            if os.path.isfile(path):
                file_hash = hashFile(path)
                if file_hash is not None:
                    hash_table[path] = file_hash
    
    except:
        print("Invalid")

    return hash_table

def generate_table(directory):
    hash_table = traverseDirectory(directory)

    file = open("hashes.json","w")
    json.dump(hash_table,file,indent = 4)
    file.close()

    print("Table generated")

def validate_hash(directory):
    try:
        file = open("hashes.json","r")
        stored = json.load(file)
        file.close()
    
    except:
        print("No table")
        return

    current_hash = traverseDirectory(directory)

    for path in stored:
        if path not in current_hash:
            print(path + " deleted")
        elif stored[path] == current_hash[path]:
            print(path + "is valid")
        else:
            print(path + "is invalid")

    for path in current_hash:
        if path not in stored:
            print(path + "is new")


def main():
    print("1 --- Generate new hash table")
    print("2 --- Verify hash")

    choice = input("Enter your choice: ")
    directory = input("Enter your directory path: ")

    if choice == "1":
        generate_table(directory)
    elif choice == "2":
        validate_hash(directory)
    else:
        print("Invalid, please pick between 1 and 2")

main()