# for loop

n = 10
for i in range(n):
    print(i)

print("=============")

for i in range(1, 6):
    print(i)

# Output = 1, 2, 3, 4, 5

print("=============")

# count by 2's
for i in range(0, 10, 2):
    print(i)

# Output = 0, 2, 4, 6, 8

print("=============")

# break and continue
for i in range(0, 10, 2):
    if i == 6:
        break
    print(i)

# Output = 0, 2, 4

print("=============")

for i in range(0, 10, 2):
    if i == 6:
        continue
    print(i)

# Output = 0, 2, 4, 8, 10

print("=============")

# while loop
count = 0
while count < 10:
    print(count)
    count += 1