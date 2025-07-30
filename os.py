import os
folder=input("enter folder name to create")
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"folder '{folder}' created")
else:
    print("folder already exists")