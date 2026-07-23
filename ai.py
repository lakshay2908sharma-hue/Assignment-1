import random 
number=[random.randint(1,100)for i in range(10)]
print("random numbers:",number)
print("even numbers:")
for num in number:
    if num%2==0:
        print(num)

print("\n")
a= "python is very easy language to learn"
print(a)
print("in reverse order:")
print(a[::-1])
print("word reversed:")
print("".join(a.split()[::-1]))