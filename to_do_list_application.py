'''
project description at:
https://learn.codingtemple.com/courses/software-engineering-core/lessons/lesson-8-mini-project-to-do-list-application/topics/mini-project-to-do-list-application/
'''

def welcome_message():
    while True:
        try:
            menu_choice = input("Welcome to the To-Do List App!\n\nMenu:\n1. Add a task\n2. View Tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n")
            if menu_choice not in ["1", "2", "3", "4", "5"]:
                raise ValueError("Value Error: Menu choice must be a number (1-5)")
            else:
                if menu_choice == "1":
                    pass
                elif menu_choice == "2":
                    pass
                elif menu_choice == "3":
                    pass
                elif menu_choice == "4":
                    pass
                else:
                    print("Thank you for using the To-Do List App. Now quitting.")
                    break
        except ValueError as ve:
            print(ve)



def add_a_task(task, status="Incomplete"):
    pass

def view_tasks():
    pass

def mark_complete(task):
    pass

def delete_task(task):
    pass

welcome_message()