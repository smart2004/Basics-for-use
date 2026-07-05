# write file
with open('file.txt', 'a') as f:
    f.write('Hello Python' '\n')


# read file
with open('file.txt', 'r') as f:
    data = f.read()
    print(data)
