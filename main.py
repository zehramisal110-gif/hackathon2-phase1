"""
TODO App - Phase 1 (AI-Driven CLI)
Hackathon 2 - In-Memory Task Management System

Features:
- Add tasks with titles
- View all tasks with status indicators
- Delete tasks by number
- Toggle task completion status
- Input validation and error handling
"""

import sys
from typing import List, Dict

# In-Memory Storage: Tasks stored in list during runtime
tasks: List[Dict[str, any]] = []


def display_menu() -> None:
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("         TODO APP - PHASE 1 (IN-MEMORY)")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Toggle Status (Complete/Incomplete)")
    print("5. Exit")
    print("=" * 50)


def add_task() -> None:
    """Add a new task to the list."""
    title = input("\nEnter task title: ").strip()
    
    if not title:
        print("❌ Error: Task title cannot be empty!")
        return
    
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print(f"✅ Task '{title}' added successfully!")


def view_tasks() -> None:
    """Display all tasks with their status."""
    if not tasks:
        print("\n📝 No tasks available. Add some tasks to get started!")
        return
    
    print("\n" + "=" * 50)
    print("                 YOUR TASKS")
    print("=" * 50)
    
    for i, task in enumerate(tasks, start=1):
        status = "✅ Complete" if task["done"] else "❌ Incomplete"
        print(f"{i}. {task['title']:<35} [{status}]")
    
    print("=" * 50)
    print(f"Total Tasks: {len(tasks)} | Completed: {sum(1 for t in tasks if t['done'])}")


def delete_task() -> None:
    """Delete a task by its number."""
    if not tasks:
        print("\n❌ No tasks to delete!")
        return
    
    view_tasks()
    
    try:
        task_num = input("\nEnter task number to delete (or 'c' to cancel): ").strip()
        
        if task_num.lower() == 'c':
            print("Deletion cancelled.")
            return
        
        idx = int(task_num) - 1
        
        if 0 <= idx < len(tasks):
            removed_task = tasks.pop(idx)
            print(f"✅ Task '{removed_task['title']}' deleted successfully!")
        else:
            print(f"❌ Error: Invalid task number. Please enter a number between 1 and {len(tasks)}.")
    
    except ValueError:
        print("❌ Error: Please enter a valid number!")


def toggle_task_status() -> None:
    """Toggle the completion status of a task."""
    if not tasks:
        print("\n❌ No tasks to update!")
        return
    
    view_tasks()
    
    try:
        task_num = input("\nEnter task number to toggle status (or 'c' to cancel): ").strip()
        
        if task_num.lower() == 'c':
            print("Status update cancelled.")
            return
        
        idx = int(task_num) - 1
        
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = not tasks[idx]["done"]
            status = "completed" if tasks[idx]["done"] else "incomplete"
            print(f"✅ Task '{tasks[idx]['title']}' marked as {status}!")
        else:
            print(f"❌ Error: Invalid task number. Please enter a number between 1 and {len(tasks)}.")
    
    except ValueError:
        print("❌ Error: Please enter a valid number!")


def exit_app() -> None:
    """Exit the application gracefully."""
    print("\n" + "=" * 50)
    print("Thank you for using TODO App - Phase 1!")
    print("Note: All tasks are stored in memory and will be lost.")
    print("=" * 50)
    sys.exit(0)


def get_user_choice() -> str:
    """Get and validate user menu choice."""
    choice = input("\nSelect an option (1-5): ").strip()
    return choice


def main() -> None:
    """Main application loop."""
    print("\n🚀 Welcome to TODO App - Phase 1 (In-Memory Storage)")
    
    menu_actions = {
        '1': add_task,
        '2': view_tasks,
        '3': delete_task,
        '4': toggle_task_status,
        '5': exit_app
    }
    
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            action = menu_actions.get(choice)
            
            if action:
                action()
            else:
                print("❌ Invalid option! Please select a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user.")
            exit_app()
        
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":

    main()
