#test.py
from main import *

expected_value =  0xAC
print(f"{hide_bits(0xAB,0xC3)=:x}, {expected_value=:x}")

expected_value = 0x13
print(f"{hide_bits(0x12,0xDF, 2)=:x}, {expected_value=:x}")
