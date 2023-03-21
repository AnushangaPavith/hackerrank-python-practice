from collections import Counter

X = int(input())
shoeListAsStr = input()

# split the string into list of strings, then convert all items to integers and create the counter
shoes = Counter(int(i) for i in shoeListAsStr.split())

N = int(input())


print(shoes)
print(shoes[5])
shoes[5] = shoes[5] - 2
print(shoes)
