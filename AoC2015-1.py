filename = "inputDay-1.txt"
try:
    fhand = open(filename)
except:
    print(f'Cannot open file: {filename}')
    exit()
text = ''
count = 0
for line in fhand:
    text = text + line
    for char in text:
        if char == '(':
            count += 1
        else:
            count -= 1
print(count)