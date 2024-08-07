HELP="""
help - напечатать справку по программе.
add - добавить задачу в список(название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.

exit -выход из программы. """
tasks=[]
run=True
while run:        #нужно сделать отступ для всего тела цикла
        command=input("Введите команду:")
        if command=="help":
            print(HELP)
        elif command=="show":
            print(tasks)
        elif command=="add":
            task=input("Ведите название задачи")
            tasks.append(task)
            print("Задача добавлена")
        elif command=="exit":
            print("Спасибо за внимание,досидания")
            run=False
        else:
            print("Неизвестная команда")
            run=False
            print("Good bye")