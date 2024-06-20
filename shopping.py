products={
    "laptop": 50000,
    "smartphone": 15000,
    "headphones": 2000,
    "keyboard": 1500,
    "mouse": 800
}

def Display_products():
    print("Available Product:")
    for item,price in products.items():
        print(f"{item.capitalize()} : {price} rs")
        
def Display_cart(cart):
    if not cart:
        print("cart is empty")
    else:
        print("your shoping cart: ")
        total_cost = 0
        for item,quantity in cart.items():
            cost = products[item]*quantity
            print(f"{item.capitalize()} x{quantity}: {cost}")
            total_cost += cost
        print(f"Total cost: {total_cost}")
def main():
    cart={}
    
    while True:
        Display_products()
        action=input("Do you want to add/remove/view/checkout (a/r/v/c)? ").lower()
        
        if action=='a':
            item=input("Enter the name of the product you want to add: ").lower()
            if item in products:
                quantity=int(input("Enter the quantity: "))
            if item in cart:
                cart[item]+=quantity
            else:
                cart[item]=quantity
            print("product not found.")
        
        elif action=='r':
            item=input("Enter the name of the product you want to remove: ").lower()
            if item in cart:
                quantity=int(input("Enter the quantity to remove: "))
                if quantity >= cart[item]:
                    del cart[item]
                    print(f"remove all {item} from yoyr cart.")
                else:
                    cart[item] -=quantity
                    print(f"remove {quantity} x {item} from your cart.")
            else:
                print("product not in cart.")
        elif action=='v':
            Display_cart(cart)
            
        elif action=='c':
            Display_cart(cart)
            confirm = input("Do you want to checkout(yes/no: ").lower() 
            if confirm=='yes':
                print("Thank you for your purchase!")
                break
        else:
            print("Invalid action. Please choose a/r/v/c.")
        
        continue_shopping = input("Do you want to continue shopping ? (yes/no): ").lower()
        if continue_shopping != 'yes':
            break
        
    print("Existing the online store. Have a great day!")
    
if __name__ ==  "__main__":
    main()

                                   
    