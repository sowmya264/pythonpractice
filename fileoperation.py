try:
    file=open('people.csv')
    str=file.readline()
    strr=file.readline()
    print(str)
    print(strr)
except IOError:
    print("error occured during input take")
else:
    print("succesfully fetched the data........")