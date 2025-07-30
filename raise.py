#raise [exception[ ,args[,traceback]]]
'''try:
    num=11
    print(num)
    raise ValueError
except:
    print("Exception occured")
    Traceback (Most recent calls)'''
#---------------------------------------


'''try:
    print("Raising exception")
    raise ValueError
except:
    print("Exception caught......")
finally:
    print("performing cleanup in finally")'''
#------------------------------------------------


'''c=int(input("enter temp in c:"))
f=(c*9/5)+32
assert(f<=32), "its cold"
print("fahrenhit:",f)'''
#------------------------------
#write a prgm which infinitely prints natural numbers in given range using raise,stopiteration and while loop

'''def display(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=' ')
i=0;
display(i)'''

#------------------------------------

import random 
class RandomError(Exception):
    pass
try:
    num=random.random()
    if num<0.1:
        raise RandomError
except RandomError as e:
    print("RandomError generated")
else:
    print("%.4f"%num)
            