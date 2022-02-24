with open('src.txt', 'r', encoding='utf-8') as f:
    lines_list = f.readlines()
lines = ''
for line in lines_list:
    lines += line
lines = lines.replace('\n', ' ')
for i in range(ord('㉠'), ord('㉻') + 1):
    lines = lines.replace(chr(i), '')
for i in range(ord('Ⓐ'), ord('ⓩ') + 1):
    lines = lines.replace(chr(i), '')
for i, j in zip(('󰡔', '󰡕'), ('<', '>')):
    lines = lines.replace(i, j)
while '  ' in lines:
    lines = lines.replace('  ', ' ')
with open('dst.txt', 'w', encoding='utf-8') as f:
    f.write(lines)
print('Done')
