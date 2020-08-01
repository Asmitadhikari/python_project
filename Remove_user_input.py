a = [1, 2, 4, 5, 6, 1, 3, 1, 8, 10, 1]
num = int(input("Enter a number you want to remove from list:"))
print(a)
for i in a:
    if num == i:
        a.remove(num)
print(a)
