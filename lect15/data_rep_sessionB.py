#Lecture 15 Data Representation 8.1 - 8.2
x = 10
y = 0b1010
q = 0b100
print(q)
print(x == y)
print(f"{x:010b}")
# Representing numbers in binary (Base 2): Digits 0/1
 
# Representing numbers in hex (Base 16):Digits: 0 - 9, A - F
z = 15
print(f"{z:x}")

for i in range(16):
    print(f"{i:04b}")

for i in range(16):
    print(f"{i:x}")

a = 0x23c
print(f"{a:b}")
print("powers of 2")
for i in range(16):
    print(f"{1<<i}")


x = 100
print(x // 2)
print(x >> 1)


x = 0b10110110
print(x)
print((x<<4)>>4)
x = (x<<4)>>4
print(f"{x:08b}")
y = x & 0b1111
y = x & 0xf
print(f"{y:08b}")
print(f"{y}")
mask = 0xf0
print((x & mask)>> 4)
print(x >> 4)








