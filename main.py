# write your code here
favorite_animals = ["cat", "fish", "dog", "monkey"]
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.pop(2)
print(favorite_animals)

# PART 2
favorite_animals.append("rabbit")
for anim in favorite_animals:
    print("i love", anim)

# PART 3
numbers = [1, 2, 3, 4, 5]
numbers_sum = 0

for num in numbers:
  numbers_sum += num
  print(numbers_sum)