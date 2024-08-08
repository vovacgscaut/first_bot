HELP="""
help - напечатать справку по программе.
add - добавить задачу в список(название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.

exit -выход из программы. """
today=[]
tomorrow=[]
other=[]
run=True
while run:        #нужно сделать отступ для всего тела цикла
        command=input("Введите команду:")
        if command=="help":
            print(HELP)
        elif command=="show":
            print("Сегодня")
            print(today)
            print("Завтра")
            print(tomorrow)
            print("Другие")
            print(other)
        elif command=="add":
            date=input("Введите дату:")
            task=input("Ведите название задачи")
            if date=="Сегодня":
                today.append(task)
                print(f"Задача {task} добавлена")
            elif date=="Завтра":
                tomorrow.append(task)
                print(f"Задача {task} добавлена")
            elif date=="Другая":
                other.append(task)
                print(f"Задача {task} добавлена")
        elif command=="exit":
            print("Спасибо за внимание,досвидания")
            break
        else:
            print("Неизвестная команда")
            run=False
            print("Good bye")