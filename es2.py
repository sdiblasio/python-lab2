from sys import argv

todo_list = list()
filename = argv[1]
txt = open(filename)
text = txt.read()
lines = text.split('\n')
for line in lines:
    todo_list.append(line)
print(todo_list)
