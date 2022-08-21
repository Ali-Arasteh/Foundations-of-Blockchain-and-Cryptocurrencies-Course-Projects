import random
import string
import hashlib as hl

def get_random_string():
    length = random.randint(1, 10)
    letters = string.ascii_letters + string.digits
    result = ''.join(random.choice(letters) for i in range(length))
    return result

strings = []
strings_hash = []
while True:
    temp = get_random_string()
    temp_hash = hl.sha256(temp.encode('UTF-8')).hexdigest()
    if len(temp_hash) > 5:
        temp_hash = temp_hash[-5:]
    if temp not in strings:
        if temp_hash in strings_hash:
            print(temp)
            print(strings[strings_hash.index(temp_hash)])
            break
        else:
            strings.append(temp)
            strings_hash.append(temp_hash)