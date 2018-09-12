
f_cry = open('密文.txt', 'r')
f_txt = open('明文.txt', 'r')

line_cry = f_cry.read()
print(line_cry)

line_txt = f_txt.read()
print(line_txt)

for i in range(0, len(line_txt)):
    print(chr(ord(line_txt[i]) ^ ord(line_cry[i])), end='')
