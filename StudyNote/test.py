print("Running through the while: ", end='')
count = 0
while count < 5:
    print(count, end='')
    count += 1
else:
    print("In the else clause of the while loop.")


print("Breaking out of the while: ", end='')
count = 0
while count < 5:
    print(count, end='')
    count += 1
    if count > 3:
        break
else:
    print("In the else clause of the early break loop.")
