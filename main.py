import random

numbers1 = []
numbers2 = []
result = []
for i in range(10):
	numbers1.append(random.randint(0,10))
	numbers2.append(random.randint(0,10))
	result.append(numbers1[len(numbers1)-1] + numbers2[len(numbers2)-1])
print(numbers1)
print("+")
print(numbers2)
print("=")
print(result)