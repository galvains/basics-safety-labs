
# Первое задание

'''
e = 95
d = 23
n = 195
m = ord('G')
print(m)

c = pow(m, e, n)
print(c)

m = pow(c, d, n)
print(m)
'''

# Второе задание
'''
name = "flag{inogda_hochetsya_prostogo_piva}"
m = int.from_bytes(name.encode(), 'big')
print('m: ', m)

p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163

n = p * q
print('n: ', n)
phi = (p - 1) * (q - 1)
print('phi: ', phi)

def func(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = func(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = func(b, n)
    print(g, x, _)

    if g == 1:
        return x % n

e = int(input('Enter your e: '))
# phi = int(input('Enter phi: '))

print(func(e, phi))
inv = mulinv(e, phi)
print('iverse', inv)

# d = 37448483950199244693343282247739490952353160187282590591081973313582331434733
# e = int(input('Enter your e: '))

c = pow(m, e, n)
print(c)

# m = pow(c, d, n)
# print(m)

print(m.to_bytes((m.bit_length() + 7) // 8, 'big').decode())
'''

# Третье задание
'''
n = 9567648541342714273618397561214215397959
e = 65537
c = 7363621633663288624203077252360225035259

p = 70636931
q = 135448247905089679980836052478189

phi = (p - 1) * (q - 1)

def func(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = func(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = func(b, n)
    print(g, x, _)

    if g == 1:
        return x % n

print(func(e, phi))
inv = mulinv(e, phi)
print('iverse', inv)

m = pow(c, 6247869887652249525823939549986133259513, n)
print(m)

print(m.to_bytes((m.bit_length() + 7) // 8, 'big').decode())
'''
# Четвертое задание

name = "flag{inogda_hochetsya_prostogo_piva}"
m = int.from_bytes(name.encode(), 'big')
print('m =', m)

e1 = 17
e2 = 13

p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163

n = p * q
phi = (p - 1) * (q - 1)

def func(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = func(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = func(b, n)
    print(g, x, _)

    if g == 1:
        return x % n

print(f'r = {func(e1, e2)[1]}; s = {func(e1, e2)[2]}')
r = -1
s = 4

def gcd(n, m):
    a, a_ = 0, 1
    b, b_ = 1, 0

    c, d = n, m

    q = c // d
    r = c % d
    while r:
        c, d = d, r
        a_, a = a, a_ - q * a
        b_, b = b, b_ - q * b

        q = c // d
        r = c % d
    return (d, a, b)


def modinv(r, m):
    g, x, y = gcd(r, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
print('n =', n)
print('c1 =', c1)
print('c2 =', c2)

g = e2 * s + e1 * r
print('g =', g)
r = (-1) * r
c1_inv = modinv(c1, m)
print('c1_inv = ' + str(c1_inv))
c1r = pow(c1_inv, r, m)
print('c1**r = ' + str(c1r))

c2s = pow(c2, s, m)
print('c2**s = ' + str(c2s))
n = 0
d = c1r * c2s
print('d = ' + str(d))
n = d % m
print('m = ' + str(m))

print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
