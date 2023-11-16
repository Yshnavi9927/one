d={}
def add_new(): # this function is used to add items
    key=input("Enter the item to be added to the inventory")
    a=int(input(f" Enter the quantity of the {key} "))
    b=float(input(f" Enter the price of {key}"))
    d[key]=({"quantity":a,"price":b})
def update_quantity(): # to update the quantity
    key=input("Enter the item in which you have to update the quantity")
    if key in d:
       d[key]["quantity"]=int(input("Enter the new quantity"))
    else:
        print(f"The given item {key} is not present")
def print_items(): # to print in items
    if len(d)>=1:
      for i in d:
        print(i,d[i])
    else:
        print("No items are there ")
def del_items(): # to delete the item
    if len(d)>=1:
       key=input("Enter the item to be deleted")
       if key in d:
          del d[key]
    else:
        print("There are no items to delete")

while 1:
    n=int(input("\nEnter\n1. to add items \n2. to update the quantity \n3. to Print the items \n4. to delete an item\n5. to exit\n"))
    if n==1:
       add_new()
    elif n==2:
       update_quantity()
    elif n==3:
        print_items()
    elif n==4:
        del_items()
    elif n==5:
        exit()
    else:
        print("Invalid choice")


