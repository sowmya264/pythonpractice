from collections import Counter
text=input("enter text:")
counter=Counter(text)
print("characters frequencies",dict(counter))