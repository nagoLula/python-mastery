import json
from typing import Any, List

def load_users() -> List[Any]:
    with open("users.json", "r") as file:
        return json.load(file)

def show_users(users: List[Any]) -> None:
    print("\nUr List:")
    for user in users:
        print(f"- {user['name']} ({user['role']})")
    
def main():
    users = load_users()
    show_users(users)
    
