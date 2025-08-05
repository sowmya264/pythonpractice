with open('file12.txt','r')as file12,open('file2.txt','r')as file2:
    content1=file12.read()
    content2=file2.read()
    print("data of file1:")
    print(content1)
    print("data of file2")
    print(content2)
    file12.close()
    file2.close()