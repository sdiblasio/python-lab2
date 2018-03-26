actions = ["insert", "remove", "show", "close"]
todo_list = list()

action = input("Please type your next action:\ninsert: to insert a new task\nremove: to remove a task\nshow: to see all existing tasks\nclose: to close the program\n")
while action != actions[3]:
    if action == actions[0]:
        task = input("Insert your todo action: ")
        todo_list.append(task)
    elif action == actions[1]:
        task = input("Insert your action to be deleted: ")
        todo_list.remove(task)
    elif action == actions[2]:
        print(todo_list.sort())
    else: print("The command inserted is not correct")
    action = input("Please insert your next command: ")