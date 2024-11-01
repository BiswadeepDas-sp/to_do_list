This Python-based To-Do List application provides an intuitive way to manage tasks. Users can create, view, delete, replace, and mark tasks as complete or incomplete. Additionally, tasks can be filtered or searched for easier navigation, and all data can be saved to or loaded from a file using Python's pickle module.

##Features
1.**Create Task**: Add new tasks to your to-do list with a default "incomplete" status.

2.**Delete Task**: Remove a task by selecting its index.

3.**Replace Task**: Update an existing task with new details.

4.**Mark Task as Complete/Incomplete**: Change the completion status of a task.

5.**Filter Tasks**: View only completed or incomplete tasks.

6.**Search Tasks**: Find tasks that contain a specified keyword.

7.**View All Tasks**: Display all tasks in a neatly formatted table.

8.**Save To-Do List**: Save the current to-do list to a file (todo_list.pkl).

9.**Load To-Do List**: Load a saved to-do list from a file.

10.**Navigate with 'B'**: Press 'B' to go back to the main menu during any input prompt.

##Requirements
-**Python 3.x**
-**Modules: os, pickle, time**
##Installation and Setup
-Make sure you have Python 3.x installed on your system.

-Clone or download this project to your local directory.

-Navigate to the project directory in your terminal.

##How to Run
-Open a terminal or command prompt in the project directory.
-Run the script using the command:

'''bash
python to_do_list.py
'''

-Follow the on-screen instructions to interact with the main menu.

##Usage Instructions

##Main Menu Options

1.Create Task: Enter the task description when prompted. The task will be added with a status of "Incomplete."

2.Delete Task: Enter the index of the task you want to delete.

3.Replace Task: Enter the index of the task you want to update, followed by the new task details.

4.Mark Task as Complete/Incomplete: Enter the index of the task, then specify if it should be marked as complete or incomplete.

5.Filter Tasks: Choose to view either completed or incomplete tasks.

6.Search Tasks: Enter a keyword to search for matching tasks.

7.View All Tasks: Displays all tasks in a formatted table.

8.Save To-Do List: Saves the current tasks to todo_list.pkl for later use.

9.Load To-Do List: Loads tasks from todo_list.pkl if it exists.
10.Exit: Closes the application.


##Notes
-To navigate back to the main menu from any input prompt, enter 'B'.
-Tasks are displayed in a structured table with their index, description, and status.
-If no tasks are present or a wrong index is entered, the program will prompt you to try again.

##Example Workflow

-Create a task by selecting option 1.
-Mark the task as complete using option 4.
-Save your list with option 8.
-Exit the program and reload your tasks next time using option 9.
#File Structure
-**to_do_list.py**: The main script for the To-Do List application.
-**todo_list.pkl**: The file where your to-do list data is saved (created after using the save feature).

#License
This project is provided "as-is" under the MIT License. You are free to modify and distribute it as you wish.

#Acknowledgements
-Python documentation for the os, pickle, and time modules.
-Inspiration from various to-do list apps for functionality design.
