numbers = [5, 2, 9, 1, 8]
target=9
find=False
for num in numbers:
    if target==num:
        find=True
        break
if find:
    print("found")
else:
    print("not found")