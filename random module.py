import random
#random 
print(random.random())
#randint
print(random.randint(1,5))
#choice
list=['hi','heloo','how','when','why']
print(random.choice(list))
print(random.choices(list))
#randrange
print(random.randrange(5,10))
print(random.randrange(5, 10, 2))
#shuffle
num=[1,2,3,4,5]
random.shuffle(num)
print(num)
#seed
random.seed(10)
print(random.randint(1,100))