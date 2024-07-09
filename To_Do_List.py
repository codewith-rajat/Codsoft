class ToDOList:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
    def update_task(self,task_number,new_task):
        try:
            self.tasks[task_number-1]=new_task
        except IndexError:
            print("Invalid index")
    def delete_task(self,task_number):
        try :
            del self.tasks[task_number-1]
        except IndexError:
            print("Invalid Index")
    def view_task(self):
        for i,task in enumerate(self.tasks,1):
            print(f"{i}. {task}")
def main():
    todolist=ToDOList()

    while True:
        print("\n\n1.Add Task")
        print("2.Update Task")
        print("3.Delete Task")
        print("4.View Tasks")
        print("5.Quit")

        choice=input("Choose an option:")

        if choice=="1":
            task=input("Enter the task:")
            todolist.add_task(task)
        elif choice=="2":
            task_number=int(input("Enter the task no.:"))
            new_task=input("Enter the new task:")
            todolist.update_task(task_number,new_task)
        elif choice=="3":
            task_number=int(input("Enter the task no.:"))
            todolist.delete_task(task_number)
        elif choice=="4": 
            todolist.view_task()
        elif choice=="5":
            break
        else:
            print("Invalid Choice")
if __name__== "__main__":
    main()
