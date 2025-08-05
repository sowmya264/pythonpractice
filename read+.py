with open('file12.txt','r+') as file:
    content=file.read()
    file.seek(10)
    file.write("modification done here")