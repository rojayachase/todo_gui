while True:
    user_action = input("Type add or show, edit, complete or exit ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter your todo?  ') + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)


            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            print(todos)

            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input('Number of the todo to edit?     '))
            number = number - 1
            new_todo = input("Enter new todo: ")
            existing_todo = todos[number]
            todos[number] = new_todo
        case 'complete':
            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
                number = int(input('Number of the todo you completed'))
                todos.pop(number -1 )
        case 'exit':
            break