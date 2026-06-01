import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks(): # type: ignore
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return 

def save_tasks(tasks): # type: ignore
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
def add_task(description: str) -> None:
    tasks = load_tasks() # type: ignore
    tasks.append({"description": description, "done" : False}) # type: ignore
    save_tasks(tasks)
    
def list_tasks():
    tasks = load_tasks() # type: ignore
    if not tasks:
        print("\nNo tasks yet.")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1): # type: ignore
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['description']}")
        
def mark_task_done(index: int) -> None: # type: ignore
    tasks = load_tasks() # type: ignore
    if 0 < index <= len(tasks): # type: ignore
        tasks[index - 1]["done"] = True # type: ignore
        save_tasks(tasks)
        print(f"\nTask {index} marked as done.")
    else:
        print("\nInvalid task number.")

  
