import random

list_a = [1,2,3,4,5]
print("random:", random.random())
print("uniform:", random.uniform(10, 20))
print("randrange:", random.randrange(10))
print("randint:", random.randint(1, 10))
print("choice:", random.choice([1,2,3,4,5]))
print("suffle:{}, {}".format(random.shuffle(list_a), list_a))
print("sample:", random.sample(list_a, 2))