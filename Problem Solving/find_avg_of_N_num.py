#Find average of N numbers in Python
num = int(input("Enter the number of elements: "))
total = 0
for _ in range(num):
    value = int(input("Enter a number: "))
    total += value
average = total / num if num > 0 else 0
print("The average is:", average)