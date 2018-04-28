from sys import argv

todo_list = list()


def startup(filename):
    txt = open(filename)
    text = txt.read()
    lines = text.split('\n')
    for line in lines:
        if len(line) > 0:
            todo_list.append(line)
    txt.close()
    #print(todo_list)


def insert():
    task = input("Insert the task to be added: ")
    todo_list.append(task)


def delete():
    task = input("Insert the task you want to delete: ")
    if task not in todo_list:
        print("The task typed was not in the list.")
    else:
        todo_list.remove(task)


def show():
    print()
    for task in sorted(todo_list):
        print(task)
    print()


def save(filename):
    txt = open(filename, 'w')
    for task in todo_list:
        txt.write(task + '\n')
    txt.close()

if __name__ == '__main__':
    startup(argv[1])
    open_ex = True
    print("Insert the number corresponding to the action you want to perform>")
    print("1. insert a new task;")
    print("2. removea task;")
    print("3. show all the tasks;")
    print("4. close the program;")
    while open_ex:
        action = int(input("Your choice: "))
        if action == 1:
            insert()
        elif action == 2:
            delete()
        elif action == 3:
            show()
        elif action == 4:
            save(argv[1])
            open_ex = False
        else:
            print("The action required is not in the range 1-4.")