def add_items():
    items = []
    
    print("Create your shopping list. Type 'done' when finished.")
    while True:
        item = input("add an item: ")
        
        if item.lower() == 'done':
            break
        
        items.append(item) # type: ignore
    return items
 

def show_list(items):
    print("\nYour Shopping List:")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item}")
        
def main():
    items = add_items()
    show_list(items)
    
if __name__ == "__main__":
    main()