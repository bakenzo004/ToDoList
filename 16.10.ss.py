# TO-DO list
import datetime
class Tasks:
    __id = 1
    def __init__(self,task_name,discription,end_time,status):
        self.task_name =task_name
        self.discription = discription
        self.end_time = end_time
        self.status = status
        self.datetime = datetime.datetime.now()
        self.id = Tasks.__id
        Tasks.__id += 1
    def __str__(self):
        return f"{self.id}) {self.task_name}   \n{self.discription}   \n{self.end_time}   \n{self.datetime.strftime('%d.%m.%Y, %H:%M')}   \n{self.status}\n"
    
class ToDoList:
    __to_do_list = []
    def add_task_to_list(self,task: Tasks):
        self.__to_do_list.append(task)
    def show_all_tasks(self):
        print(*self.__to_do_list)
    def update_task(self,id):
        for task in self.__to_do_list:
            if task.id == id:
                print("Что вы хотите обнавит?:\n 1)Имя задачи\n2)Описание\n3)Время завершения\n4)Статус")
                x = int(input())
                if x == 1:
                    task.task_name = input("Имя задачи:")
                if x == 2:
                    task.discription = input("Описание")
                if x == 3:
                    task.end_time = input("Время завершения:")
                if x == 4:
                    task.status = input("Статус:")
                else:
                    print("Только 4 варианта!!!")
                print("Редактирование прошло успешно")
    def delete_task(self,id):
        for task in self.__to_do_list:
            if task.id == id:
                self.__to_do_list.remove(task)
                print("Удаление завершено успешно")
    def save_tasks(self):
        with open("to_do_list.txt",encoding= "utf-8",mode="a") as file:
            for task in self.__to_do_list:
                file.write(task.__str__())

            print("Сохранение прошло успешно")

    def filter_list_status(self):
        for task in self.__to_do_list:
            print(f"||{task.status}||")
            if task.status.strip().lower() == "выполнено":
                print("выполненные задачи:")
                print(f"\n {task}")
            else:
                print("Не выполненные задачи:")
                print(f"\n{task}")
    def filterr(self,task):
        if task.status.strip().lower() == "выполнено":
            return True
        return False
    
    def filt(self):
        print(*filter(self.filterr,self.__to_do_list))

    def filterr2(self,task):
        if task.status.strip().lower() == "выполнено":
            return False
        return True
    
    def filt2(self):
        print(*filter(self.filterr2,self.__to_do_list))


    def read_txt(self):
        with open ("to_do_list.txt",encoding="utf-8",mode="r") as file:
            for task in file.readlines():
                print(*task)

    def poisk(self,poisk):
        for task in self.__to_do_list:
            k = str(task).find(poisk)
            if k == -1:
                continue
            else:
                print(task)

while True:
    print("Выбери действие:")
    print("""
1) Добавить задачу 
2) Редактировать задачу
3) Просмотр задач 
4) Удаление задачи 
5) Сохранение задачи
6) Выполненые задачи
7) Не выполненые
8) Читать с файла txt
9) Поиск
10) Выйти из приложения 
          """)
    n = input()
    lst = ToDoList()
    if n == "1":
        print("Добавит задачу:")
        x = Tasks(task_name=input("Имя задачи:\n"),discription=input("Описание:\n"),end_time=input("dd.mm.year, hh:mm:\n"),status=input("Статус: выполнено/не выполнено\n"))
        lst.add_task_to_list(x)
        print("Задача добавлена успешно")
        print()
    if n == "2":
        i = int(input("Введите id задачи для редактирования:\n"))
        lst.update_task(i)
        print()
    if n == "3":
        lst.show_all_tasks()
        print()
    if n == "4":
        f = int(input("Введите id задачи для удаления:\n"))
        lst.delete_task(f)
        print()
    if n == "5":
        lst.save_tasks()
        print()
    if n == "6":
        lst.filt()
        print()
    if n == "7":
        lst.filt2()
        print()
    if n == "8":
        lst.read_txt()
    if n == "9":
        p = input("Введите слово для поиска:\n")
        lst.poisk(p)
        print()
    if n == "10":
        print("Досвидание!")
        break