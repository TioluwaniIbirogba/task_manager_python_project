import json
class TaskManager:
    def __init__(self):
        try:
            with open("task_manager.json", "r", encoding='utf-8') as file:
                tasks = json.load(file)

        except FileNotFoundError:
            self.__task_list = []
            self.__task_done_list = []
        else:
            self.__task_list = tasks["To Do"]
            self.__task_done_list = tasks["Done"]

    @property
    def task_list(self):
        return self.__task_list

    @property
    def task_done_list(self):
        return self.__task_done_list
    
    def add_task(self, task):
        self.__task_list.append(task)
        return "Task added!"

    def task_completed(self, task):
        response = "Task does not exist"
        task_list = self.__task_list
        if self.__task_list == []:
            return("No tasks available.")
        for t in task_list:
            if t.lower() == task.lower():
                self.__task_done_list.append(t)
                self.__task_list.remove(t)
                response = "Task is marked as completed."

        return response

    def delete_task(self, task):
        response = "Task does not exist"
        task_list = self.__task_list
        for t in task_list:
            if t.lower() == task.lower():
                self.__task_list.remove(t)
                response = "Task is removed."
        return response

def menu_display():
    return " ---    Tasks List Menu    --- \n| 1 - View tasks list         |\n| 2 - Add task                |\n| 3 - Mark task as completed  |\n| 4 - Delete task             |\n| 5- Exit progam              |"

task_manager = TaskManager()
while True:
    task_dict = {"To Do": task_manager.task_list,                
   "Done": task_manager.task_done_list} ##Tech With Tim. (2022, 25 Jan). How To Use JSON In Python[video]. Youtube. https://www.youtube.com/watch?v=-51jxlQaxyA
    print(menu_display())
    try:
        choice = int(input("| Enter here: "))
    except ValueError:
        print(("| Write the number of your choice") + menu_display())
    else:
        if choice == 5:
            with open('task_manager.json', 'w') as file:
                json.dump(task_dict, file)
            print("Have a nice day!")
            break

        else:
            if choice == 1:
                print("To do: ")
                task_num = 0
                for task in task_manager.task_list:
                    task_num += 1
                    print(f"{task_num}- {task}")
                print(f"Done:")
                task_done_num = 0
                for task_done in task_manager.task_done_list:
                    task_done_num += 1
                    print(f"{task_done_num}- {task_done}")
            elif (choice == 2) or (choice == 3):
                if choice == 2:
                    more_task = input('| Write: ')
                    print(task_manager.add_task(more_task))

                elif choice == 3:
                    task_1 = input('| Write: ')
                    print(task_manager.task_completed(task_1))

            elif choice == 4:
                task_2 = input('| Write: ')
                print(task_manager.delete_task(task_2))
                        