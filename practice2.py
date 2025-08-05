'''arr=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in arr:
    sum+=i
print(sum)'''
#----------------------------------
'''arr=[]
print("enter 20 intege values")
for i in range(20):
    num=int(input(f"enter number{i+1}:"))
    arr.append(num)
arr_max=arr.copy()
arr_min=arr.copy()
for i in range(3):
    max_val=max(arr_max)
    print(max_val)
    arr_max.remove(max_val)
for i in range(3):
    min_val=min(arr_min)
    print(min_val)
    arr_min.remove(min_val)'''
#-----------------------------------------
'''arr=[int(input())for i in range(10)]
print(arr[::-1])'''
#------------------------------------------
'''count=[0]*101
for i in range(30):
    mark=int(input(f"enter marks {i+1}"))
    if 0<=mark<=100:
        count[mark]+=1
    else:
        print("invalid mark")
        i-=1
for mark in range(101):
    if count[mark]>0:
        print(f"mark {mark}={count[mark]} students(s)")'''
#---------------------------------------------------
'''rows=10
for i in range(1, rows + 1):
    for num in range(1, i + 1):
        print(num, end="")
    for j in range(i - 1, -1, -1):
        print(chr(64 + j), end="")
    print()'''
#---------------------------------------------
'''count=0
for i in range(1,4):
    mark=int(input(f"enter marks for student{i}"))
    if 0<=mark<=100:
        if mark>=35:
            count+=1
    else:
        print("invalid")
        i-=1
print(f"students who passed {count}")'''
#--------------------------------------------------
#count number of digits
'''n=123
count=0
while n!=0:
    n=n//10
    count+=1
print(count)'''
#-----------------------------
#sum of digits
'''num=int(input())
sum=0
while num!=0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)'''
#-----------------------------
#decimal to binary
'''def d_b(decimal):
    if decimal==0:
        return "0"
    binary=""
    while decimal>0:
        rem=decimal%2
        binary=str(rem)+binary
        decimal=decimal//2
    return binary
num=int(input("enter the number"))
print(d_b(num))'''
#---------------------------------
#smallest ecact divisor other than one
'''def small_divisor(num):
    if num<=1:
        return "no valid divisor"
    for i in range(2,num//2+1):
        if num%i==0:
            return i
    return "number is prime"
num=int(input("enter the number"))
result=small_divisor(num)
print(result)'''
#------------------------------------
str=input()
print(str[::-1])
