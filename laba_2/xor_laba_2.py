cipher = '20263f0b1c060a2614151713260611110b26050706140c1c09'
key = '63727970746372797074637279707463727970746372797074'

def function(a):
    res = []
    for i in range(0, len(a), 2):
        elem = '0x' + a[i:i + 2]
        res.append(int(elem, 16))
    return res

cipher = function(cipher)
key = function(key)

result = [chr(cipher[i] ^ key[i]) for i in range(len(cipher))]
print(''.join(result))
