def collect_user_info():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    city = input("Please enter your city: ")
    
    return name, age, city

def summarize_user(name, age, city): # type: ignore
    print(f"\nSummary:")
    print(f"- Name: {name}")
    print(f"- Age: {age}")
    print(f"- City: {city}")
    
def main():
    name, age, city = collect_user_info()
    summarize_user(name, age, city)
    
if __name__ == "__main__":
    main()