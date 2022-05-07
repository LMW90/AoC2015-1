# assign file from same folder to variable
filename = "inputDay-1.txt"
# try creating file handler
try:
    fhand = open(filename)
except:
    print(f'Cannot open file: {filename}')
    exit()
# create variable to load text file content
text = ''
count = 0
# save read lines to a variable
for line in fhand:
    text = text + line
    # read chars from a variable - works within outer loop only cause there is only one line in a text file
    for char in text:
        if char == '(':
            count += 1
        else:
            count -= 1
print(count)