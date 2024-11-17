#Lecture 15 Data Representation 8.1 - 8.2
x = 0x10A
print(x)
y = 0b1010
print(y)

z = 10
print(y == z)
print("Numbers in binary")
for i in range(16):
    print(f"{i:04b}")

print("Numbers in hex")
for i in range(16):
    print(f"{i:x}")


for i in range(15):
    print(1 <<  i)

print(255 >> 1)
print(255 // 2)
x =   0b10101101
mask = 0b11110000
mask = 0xF0
result = x & mask
print(f"{result:08b}")
print(f"{result>>4:x}")
print(f"{(x & 0xf0)>>4:b}") # extracting bits from index 4 to 7
print(f"{result>>4:04b}")
# print bottom four bits
print(f"{x & 0xF:0b}")
    
