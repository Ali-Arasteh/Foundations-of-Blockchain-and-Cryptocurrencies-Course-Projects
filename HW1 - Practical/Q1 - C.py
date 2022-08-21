import hashlib as hl

s = 'Secret Key'
m = 'some message'
def sender(m, s):
    authentication = hl.sha256((m + s).encode('UTF-8')).hexdigest()
    if len(authentication) > 5:
        authentication = authentication[-5:]
    return [m, authentication]

def receiver(sent_message, s):
    authentication = hl.sha256((sent_message[0] + s).encode('UTF-8')).hexdigest()
    if len(authentication) > 5:
        authentication = authentication[-5:]
    if authentication == sent_message[1]:
        print(sent_message[0])
    else:
        print('The message has been changed!')

sent_message = sender(m, s)
print('The sent message =', sent_message)
receiver(sent_message, s)