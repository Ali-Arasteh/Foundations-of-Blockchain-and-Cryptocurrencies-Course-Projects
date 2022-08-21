import random
import string
import hashlib as hl

def get_random_string():
    length = random.randint(1, 10)
    letters = string.ascii_letters + string.digits
    result = ''.join(random.choice(letters) for i in range(length))
    return result

value = hl.sha256(b'96101165').hexdigest()
if len(value) > 5:
    value = value[-5:]
while True:
    random_string = get_random_string()
    random_string_hash = hl.sha256(random_string.encode('UTF-8')).hexdigest()
    if len(random_string_hash) > 5:
        random_string_hash = random_string_hash[-5:]
    if random_string_hash == value:
        break
fileID = open('x.txt', 'w')
fileID.write('96101165' + '\n')
fileID.write(random_string)
fileID.close()