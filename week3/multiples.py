def multiples():
    for i in range(1,50):
        if ((i % 3 ==0) or (i %5 ==0)):
            print(i)

multiples()



sum = 0
i = 0

def condition(i):
    return ((i % 3 ==0) or (i %5 ==0))

while i < 200:
    if condition(i):
        sum = sum + i 
    i = i + 1

print(f"sum of all numbers is {sum}")

