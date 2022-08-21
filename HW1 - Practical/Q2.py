import hashlib as hl
import math

n = input("Enter number of leaves: ")
if n.isnumeric():
    n = int(n)
    if n <= 0:
       raise Exception('n must be positive') 
else:
    raise Exception('Not a Number')
string = []
N = 2 ** math.ceil(math.log(int(n), 2))
for i in range(1, N + 1):
    if i <= n:
        if i == 1:
            string.append(input("Enter first string: "))
        else:
            string.append(input("Enter next string: "))
    else:
        string.append(string[2 * n - i - 1])
for i in reversed(range(int(math.log(N, 2)) + 1)):
    if i == int(math.log(N, 2)):
        for j in range(2 ** i):
            string[j] = hl.sha256(string[j].encode('UTF-8')).hexdigest()
    else:
        temp = []
        for j in range(2 ** i):
            temp.append(hl.sha256((string[2 * j] + string[2 * j + 1]).encode('UTF-8')).hexdigest())
        string = temp
    print(string)
print(string[0])
