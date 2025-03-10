class task:
   
   def __init__(self,name, task_id):
      self.name = name
      self.index= task_id
      self.isDone = False

class todolist:
    
        tasklist=[]  
        def add(self):
            while True:
                task_name=input("\nEnter the task you want to add or type \"exit\" to stop:   ")
                if task_name.lower()=='exit':
                    break
                else:
                    
                    count = len(self.tasklist)
                    addedTask = task(task_name, count+1)
                    self.tasklist.append(addedTask)
        def delete(self):
           
            self.show()  
            try:
                rem = int(input("\nEnter the task number you want to remove: "))
                found_element = False

               
                for i, task_from_list in enumerate(self.tasklist):
                    if task_from_list.index == rem:
                        found_element = True
                        del self.tasklist[i]
                        print(f"Task {rem} removed!")
                        break  

                if not found_element:
                    print("Invalid input")

               
                for i, task in enumerate(self.tasklist):
                    task.index = i + 1  

            except ValueError:
                print("Please enter a valid number.")

            self.show()  # Show updated task list
        def show(self):
            for task in self.tasklist:
                status="DONE" if task.isDone else "NOPE"
                print(f"\n {task.index}. {task.name}-{status}") 
        def done(self):
            task_not_done=int(input("Enter the task to be marked as done: "))
            
            for task in self.tasklist:
                if task.index == task_not_done:
                    task.isDone=True
                    print(f"{task.index} marked as done")
                    self.show()
                    return
                    break
                    
                else:
                    print("Invalid output")
                self.show()
        def leave(self):
            print("EXITING!")
            
        
    
todo=todolist()

def main():
    while True:
        print("\n\n1. Add a task")
        print("2. remove a task")
        print("3. show tasklists")
        print("4. Mark a tasklist as done")
        print("5. Exit")
        choice=int(input("\nEnter your choice:  "))
        if choice==1:
            todo.add()
        elif choice==2:
            todo.delete()
        elif choice==3:
            todo.show()
        elif choice==4:
            todo.done()
        elif choice==5:
            todo.leave()
            break
        else:
            print("Inavlid output")
        
main()