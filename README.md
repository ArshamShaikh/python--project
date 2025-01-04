# To-Do List Application with Python

Welcome to the To-Do List Project! This project is a command-line application that helps users manage their tasks effectively. 
The program allows users to add tasks, mark them as complete, delete them, and view the progress of task completion with a visual progress bar. 
The application is built in Python and uses the `colorama` and `tqdm` libraries for enhanced user experience.

## Features

- **Add Tasks**: Users can add tasks with a description.
- **View Tasks**: Display all tasks along with their status (complete/incomplete).
- **Mark Tasks as Complete**: Update the status of tasks once completed.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Progress Bar**: Visual progress bar displays the percentage of tasks completed.
- **Color-Coded Output**: Uses `colorama` to highlight task statuses and progress.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `colorama` library (for color-coded text)
- `tqdm` library (for progress bar)

### Installing Dependencies

To install the necessary libraries, run the following commands:

```bash
pip install colorama
pip install tqdm
```

##

The application presents a menu with options for managing tasks:

1. **Add Task**: Enter the description of the task to add.
2. **View Tasks**: Lists all tasks with their status.
3. **Complete Task**: Select a task to mark as complete.
4. **Delete Task**: Choose a task to remove.
5. **Exit**: Close the application.

### Example Output

```
--- To-Do List ---
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Select an option: 1
Enter task description: Finish the project report

Task added successfully!
```

### Progress Bar Example

When viewing tasks, the completion percentage is shown with a progress bar:

```
Tasks Completed: 2/5
[##########----------] 40%
```

## Additional Features (Optional Enhancements)

- **Due Dates**: Add optional due dates to tasks.
- **Priority Levels**: Allow users to assign priority levels to tasks.
- **Search or Filter**: Add a search functionality to filter tasks.

## Acknowledgements

- Python for providing an amazing programming language.
- `colorama` for enabling text colorization.
- `tqdm` for the progress bar functionality.



