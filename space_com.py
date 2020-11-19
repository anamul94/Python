
even = []
for i in range(0,1001):
    #print(i)
    if i % 2 == 0:
        even.append(1)

    else:
        even.append(0)

n = int(input("enter number to check : "))
if even[n]:
    print('yes')
else:
    print('odd')
