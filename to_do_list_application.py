'''
project description at:
https://learn.codingtemple.com/courses/software-engineering-core/lessons/lesson-8-mini-project-to-do-list-application/topics/mini-project-to-do-list-application/
'''

# Organize your code into functions to promote modularity and readability.

# making function where each other function will be accessed. Allow users to interact with the application by selecting menu options using input().
def welcome_message():
    print("Welcome to the To-Do List App!")
    while True:
        # Implement error handling using try, except, and else blocks to handle potential issues.
        try:
            menu_choice = input("\nMenu:\n1. Add a task\n2. View Tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n")
            # Implement input validation to handle unexpected user input gracefully.
            if menu_choice not in ["1", "2", "3", "4", "5"]:
                raise InputEntryError("Input Entry Error: Menu choice must be a number (1-5)")
        except InputEntryError as ve:
            print(ve)
        # covering my bases in case of unexpected error.
        except Exception as e:
            print("Unexpected Error: {e}.")
        else:
            if menu_choice == "1":
                new_task = input("What task would you like to add to your To-Do list? ").lower()
                add_a_task(new_task)
            elif menu_choice == "2":
                view_tasks()
            elif menu_choice == "3":
                updated_task = input("What task would you like to mark as complete? ").lower()
                change_status(updated_task)
            elif menu_choice == "4":
                task_to_delete = input("What task would you like to delete? ").lower()
                delete_task(task_to_delete)
            # Quitting the application.
            else:
                print("Thank you for using the To-Do List App. Now quitting.")
                break

# Adding a task with a title (by default “Incomplete”).
def add_a_task(task, status="Incomplete"):
    try:
        if task in todos:
            raise RedundancyError("Redundancy Error: Task already in list.")
        elif task == "":
            raise ZeroItemsError("Zero Items Error: New task must be at least 1 character in length.")
    except RedundancyError as re:
        print(re)
    except ZeroItemsError as ze:
        print(ze)
    else:
        todos[task] = status
        return print(f"{task} successfully added to To-Do list.")
    # Implement finally blocks to handle potential issues.
    finally:
        print("\n\nReturning to menu.")

    
# Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
def view_tasks():
    if len(todos) == 0:
        print("To-Do list empty.")
    else:
        print("TO-DO LIST:")
        for key, value in todos.items():
            print(f"{key}: {value}")
    return print("\n\nReturning to menu.")
    
# Marking a task as complete.
def change_status(task, status="Complete"):
    try:
        if len(todos) == 0:
            print("To-Do list empty.")
        elif task not in todos:
            raise InvalidTargetError("Invalid Target Error: Task not in To-Do list.")
    except InvalidTargetError as ie:
        return print(ie)
    else:
        todos[task] = status
        return print(f"{task} successfully marked as complete in To-Do list.")
    finally:
        print("\n\nReturning to menu.")
    
# Deleting a task.
def delete_task(task):
    try:
        if len(todos) == 0:
                print("To-Do list empty.")
        elif task not in todos:
            raise InvalidTargetError("Invalid Target Error: Task not in To-Do list.")
    except InvalidTargetError as ie:
        return print(ie)
    else:
        todos.pop(task)
        return print(f"{task} successfully removed from To-Do list.")
    finally:
        print("\n\nReturning to menu.")


# making custom error classes to be more descriptive and for the heck of it!
class InputEntryError(Exception):
    pass

class RedundancyError(Exception):
    pass

class InvalidTargetError(Exception):
    pass

class ZeroItemsError(Exception):
    pass

# making empty task dictionary
todos = {}

#runnin' this sucker!
welcome_message()