num=int(input("enter the numerator:"))
deno=int(input("enter the denominator:"))
try:
    quo=num/deno
    print("quotient",quo)
except ZeroDivisionError:
    print("denominator cant be zero")


#------------------------------------------


try:
    num=int(input("enter number:"))
    print(num*4)
except (KeyboardInterrupt,ValueError,TypeError):
    print("number sholud be entered...program terminated!!!!")
print("Bye")