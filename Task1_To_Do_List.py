import json
import os

# Class to manage the To-Do list
class ToDoList:
    def __init__(self, filename='task_2_todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
   
    def load_tasks(self):
        # Load tasks from a JSON file, if exists
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    
    def save_tasks(self):
        # Save tasks to a JSON file
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, name, description, due_date):
        # Add a new task to the list
        task = {
            'name': name,
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{name}' added successfully!")

    def edit_task(self, task_name, new_name=None, new_description=None, new_due_date=None):
        # Edit an existing task
        for task in self.tasks:
            if task['name'] == task_name:
                if new_name:
                    task['name'] = new_name
                if new_description:
                    task['description'] = new_description
                if new_due_date:
                    task['due_date'] = new_due_date
                self.save_tasks()
                print(f"Task '{task_name}' updated successfully!")
                return
        print(f"Task '{task_name}' not found.")
    
    def delete_task(self, task_name):
        # Delete a task from the list
        self.tasks = [task for task in self.tasks if task['name'] != task_name]
        self.save_tasks()
        print(f"Task '{task_name}' deleted successfully!")

    def mark_task_complete(self, task_name):
        # Mark a task as complete
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                self.save_tasks()
                print(f"Task '{task_name}' marked as complete!")
                return
        print(f"Task '{task_name}' not found.")
    
    def view_tasks(self):
        # View all tasks, showing their completion status
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- To-Do List ---")
        for i, task in enumerate(self.tasks, 1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i}. {task['name']} - Due: {task['due_date']} | Status: {status}")
            print(f"   Description: {task['description']}")
        print("-------------------")
    
    def view_pending_tasks(self):
        # View only pending tasks
        pending_tasks = [task for task in self.tasks if not task['completed']]
        if not pending_tasks:
            print("No pending tasks.")
            return

        print("\n--- Pending Tasks ---")
        for i, task in enumerate(pending_tasks, 1):
            print(f"{i}. {task['name']} - Due: {task['due_date']}")
            print(f"   Description: {task['description']}")
        print("---------------------")


# Command-line interface for the To-Do List
def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. Mark a task as complete")
        print("5. Edit a task")
        print("6. Delete a task")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            # Add new task
            name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (e.g., 2024-10-21): ").strip()
            todo.add_task(name, description, due_date)
        
        elif choice == '2':
            # View all tasks
            todo.view_tasks()
        
        elif choice == '3':
            # View only pending tasks
            todo.view_pending_tasks()
        
        elif choice == '4':
            # Mark task as complete
            task_name = input("Enter task name to mark as complete: ").strip()
            todo.mark_task_complete(task_name)
        
        elif choice == '5':
            # Edit task
            task_name = input("Enter task name to edit: ").strip()
            new_name = input("Enter new task name (leave empty to keep the same): ").strip() or None
            new_description = input("Enter new task description (leave empty to keep the same): ").strip() or None
            new_due_date = input("Enter new due date (leave empty to keep the same): ").strip() or None
            todo.edit_task(task_name, new_name, new_description, new_due_date)
        
        elif choice == '6':
            # Delete task
            task_name = input("Enter task name to delete: ").strip()
            todo.delete_task(task_name)
        
        elif choice == '7':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
