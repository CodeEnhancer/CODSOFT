print("----WELCOME TO TASK MANAGER APP----")
tasks=[]
total_task=input("Enter how many task you need to perform:")
count=int(total_task)
for i in range(1,count+1):
        task_name=input(f"Enter the task {i} =")
        tasks.append(task_name)

print(f"Today's tasks are\n{tasks}")

while(True):
    operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit"))
    if (operation==1):
            add=input("Enter the tasks you need to add")
            tasks.append(add)
    elif(operation==2):
            updated_val=input("Enter the task name you want to update= ")
            if updated_val in tasks:
                up=input("Enter new task: ")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated value is {up}")
    elif(operation==3):
            del_val=input("Enter the task you want to delete = ")
            if del_val in tasks:
               ind= tasks.index(del_val)
               del tasks[ind]
            print(f"deleted value is {del_val}")
    elif(operation==4):
            print(f"total tasks ={tasks}")
    elif(operation==5):
            print("Closing the program...")
            break
    else:
            print("Invalid input")
