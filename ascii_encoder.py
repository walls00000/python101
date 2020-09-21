## Give credit to this discussion on stackoverflow:
## https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

import binascii


print("Type a message to encode ")
ascii_string = input()
print("encoding " +  ascii_string)


binary = bin(int.from_bytes(ascii_string.encode(), 'big'))
print("binary: " + binary)

n = int(binary, 2)
decoded = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print("decoded: " + decoded);
