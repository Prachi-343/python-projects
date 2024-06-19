menu={   
    "pizza":100,
    "coffee":50,
    "burgur":70,
    "sandwitch":40,
    "fries":30,
    "tea":20
}
print("*******************************")
print("Welcome to Prachi's Cafe")

for i in menu:
    print(f"{i} :{menu[i]}rs")

total_bill=0
item_1=input("\nEnter the name of item you want to order: ").lower()
if item_1 in menu:
    total_bill+=menu[item_1]    
    print(f"\nyour order {item_1} is received successfully")
else:
    print(f"\nYour order {item_1} is not avaialable now")

another_order=input("You want anything else?(Yes/No)").lower()
if another_order == "yes":
    item_2=input("\nEnter the name of item you want to order:").lower()
    if item_2 in menu:
        total_bill+=menu[item_2]
        print(f"\nyour order {item_2} is received successfully")
    else:
        print(f"\nYour order {item_2} is not avaialable now")
        
print(f"Your total bill is: {total_bill}rs")
print("Thanks for Visiting....")
print("*******************************")        
                 
                 
                 
                 
                 
                 
                 
                 
            

