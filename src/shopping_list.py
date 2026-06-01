def add_items(): # pyright: ignore[reportUnknownParameterType]
    items = []
    
    print("Create your shopping list. Type 'done' when finished.")
    while True:
        item = input("add an item: ")
        
        if item.lower() == 'done':
            break
        
        items.append(item) # type: ignore
    return items # type: ignore
 

def show_list(items): # type: ignore
    print("\nYour Shopping List:")
    for idx, item in enumerate(items, start=1): # pyright: ignore[reportUnknownArgumentType, reportUnknownVariableType]
        print(f"{idx}. {item}")
        
def main():
    items = add_items() # type: ignore
    show_list(items)
    
if __name__ == "__main__":
    main()