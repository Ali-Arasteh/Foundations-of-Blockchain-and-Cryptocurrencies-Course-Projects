import hashlib as hl
import math

n = input("Enter number of leaves: ")
if n.isnumeric():
    n = int(n)
    if n <= 0:
       raise Exception('n must be positive') 
else:
    raise Exception('Not a Number')
k = input("Enter place of message: ")
if k.isnumeric():
    k = int(k)
    if k <= 0 or k > n:
       raise Exception('k must be positive and smaller than or equal to n') 
else:
    raise Exception('Not a Number')
string = []
N = math.ceil(math.log(int(n), 2))
for i in range(N + 2):
    if i == 0:
        string.append(input("Enter message: "))
    elif i < N + 1:
        if i == 1:
            string.append(input("Enter first hash value: "))
        else:
            string.append(input("Enter next hash value: "))
    else:
        mr = input("Enter Merkle root value: ")
for i in range(N + 1):
    if i == 0:
        temp = hl.sha256(string[i].encode('UTF-8')).hexdigest()
    else:
        flag = ((k - 1)//2 ** (i - 1)) % 2
        if flag:
            temp = hl.sha256((string[i] + temp).encode('UTF-8')).hexdigest()
        else:
            temp = hl.sha256((temp + string[i]).encode('UTF-8')).hexdigest()
if temp == mr:
    print("Exsited")
else:
    print("Did not exist!")