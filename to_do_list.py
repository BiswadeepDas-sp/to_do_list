import os
import pickle
import time

class UserInput:
    def input_task(self):
        task = {'task': input('Enter your task: ').strip(), 'completed': False}
        if task['task'].lower() == 'b':
            return None  # Return None if user wants to go back
        return task

    def input_index(self, num: int):
        while True:
            index = input('Enter index of the task: ').strip()
            if index.lower() == 'b':
                return None  # Return None if user wants to go back
            try:
                index = int(index)
                if 1 <= index <= num:
                    return index
                else:
                    print('Index must be within the valid range.')
            except ValueError:
                print('Index must be an integer.')

    def input_status(self):
        while True:
            status = input("Enter 'C' to mark complete or 'I' for incomplete: ").strip().lower()
            if status == 'b':
                return None  # Return None if user wants to go back
            if status in ['c', 'i']:
                return status == 'c'
            print('Invalid input. Please enter "C" or "I".')

    def input_filter(self):
        while True:
            filter_by = input("Enter 'C' for completed tasks or 'I' for incomplete tasks: ").strip().lower()
            if filter_by == 'b':
                return None  # Return None if user wants to go back
            if filter_by in ['c', 'i']:
                return filter_by == 'c'
            print('Invalid input. Please enter "C" or "I".')

    def input_query(self):
        query = input('Search task: ').strip()
        if query.lower() == 'b':
            return None  # Return None if user wants to go back
        return query

class ToDoList(UserInput):
    def __init__(self):
        self.list = []
        super().__init__()

    @property
    def num(self):
        return len(self.list)

    def create_task(self):
        user_input = self.input_task()
        if user_input:
            self.list.append(user_input)
            print('Task successfully created')
        time.sleep(0.75)
        self.view(self.list)

    def delete_task(self):
        if self.num == 0:
            print("No tasks to delete.")
            return
        index = self.input_index(self.num)
        if index:
            self.list.pop(index - 1)
            print('Task deleted')
        self.view(self.list)

    def replace_task(self):
        if self.num == 0:
            print("No tasks to replace.")
            return
        index = self.input_index(self.num)
        if index:
            self.list[index - 1] = self.input_task()
            print('Task replaced')
        self.view(self.list)

    def mark_complete(self):
        if self.num == 0:
            print("No tasks to mark.")
            return
        index = self.input_index(self.num)
        if index is not None:
            self.list[index - 1]['completed'] = self.input_status()
            print('Task marked as complete')
        self.view(self.list)

    def filter_tasks(self):
        filter_by_complete = self.input_filter()
        if filter_by_complete is not None:
            filtered_list = [task for task in self.list if task['completed'] == filter_by_complete]
            self.view(filtered_list)

    def search(self):
        query = self.input_query()
        if query is not None:
            search_result = [task for task in self.list if query.lower() in task['task'].lower()]
            self.view(search_result)

    def view(self, to_view_list):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('_' * 100)
        print(f"{'Index':<10}{'Task':<70}{'Status':<15}")
        print('_' * 100)
        for index, task in enumerate(to_view_list, 1):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f"{index:<10}{task['task']:<70}{status:<15}")
        print('_' * 100)
        
    def save(self, filename="todo_list.pkl"):
        """Saves the to-do list to a file using pickle."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.list, file)
            print(f"To-do list saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving: {e}")
            
    def load(self, filename="todo_list.pkl"):
        """Loads the to-do list from a file using pickle."""
        if os.path.exists(filename):
            try:
                with open(filename, "rb") as file:
                    self.list = pickle.load(file)
                print(f"To-do list loaded from {filename}.")
                self.view(self.list)
            except Exception as e:
                print(f"An error occurred while loading: {e}")
        else:
            print(f"No saved file found at {filename}.")

class MainMenu:
    def __init__(self):
        self.todo_list = ToDoList()

    def display_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Create Task")
            print("2. Delete Task")
            print("3. Replace Task")
            print("4. Mark Task as Complete/Incomplete")
            print("5. Filter Tasks")
            print("6. Search Tasks")
            print("7. View All Tasks")
            print("8. Save To-Do List")
            print("9. Load To-Do List")
            print("10. Exit")

            choice = input("Choose an option (1-10): ").strip()

            if choice == '1':
                self.todo_list.create_task()
            elif choice == '2':
                self.todo_list.delete_task()
            elif choice == '3':
                self.todo_list.replace_task()
            elif choice == '4':
                self.todo_list.mark_complete()
            elif choice == '5':
                self.todo_list.filter_tasks()
            elif choice == '6':
                self.todo_list.search()
            elif choice == '7':
                self.todo_list.view(self.todo_list.list)
            elif choice == '8':
                self.todo_list.save()
            elif choice == '9':
                self.todo_list.load()
            elif choice == '10':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 10.")

# Running the main menu
if __name__ == "__main__":
    menu = MainMenu()
    menu.display_menu()
       
            
