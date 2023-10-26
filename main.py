items = []
numbers = []

def add_item():
    item_name = input("Enter the item name: ")
    number = float(input("Enter the associated number: "))
    items.append(item_name)
    numbers.append(number)

def remove_item():
    print("Items in the collection:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    index = int(input("Enter the location of the item you want to remove: ")) - 1
    del items[index]
    del numbers[index]

def insert_item():
    print("Items in the collection:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    index = int(input("Enter the location where you want to insert the item: ")) - 1
    item_name = input("Enter the item name: ")
    number = float(input("Enter the associated number: "))
    items.insert(index, item_name)
    numbers.insert(index, number)

def swap_items():
    print("Items in the collection:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    index1 = int(input("Enter the location of the first item: ")) - 1
    index2 = int(input("Enter the location of the second item: ")) - 1
    items[index1], items[index2] = items[index2], items[index1]
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

def find_max():
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i
    print(f"The item with the maximum value is '{items[max_index]}' with a value of {numbers[max_index]}")

def print_collection():
    print("Collection:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item} - {numbers[i-1]}")

print("Welcome to the List App!")

while True:
    print("\nMenu:")
    print("1. Add an item to the end of the collection")
    print("2. Remove an item from the collection")
    print("3. Insert an item into the collection")
    print("4. Swap two items in the collection")
    print("5. Search the collection for the item with the maximum value")
    print("6. Print the full collection")
    print("7. Quit the application\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        insert_item()
    elif choice == "4":
        swap_items()
    elif choice == "5":
        find_max()
    elif choice == "6":
        print_collection()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")