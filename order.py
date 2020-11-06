# Import the menu class
from menu import Menu
# Create the Order class which is a child of Menu
class Order(Menu):

    def __init__(self):
        # Inherit parent attributes using super
        super().__init__()
        # Ask the customer for their name, to personalise the experience
        self.customer=input("Please enter your name: ").capitalize()
        # Define waiter/waitress name here so can easily be changed for different servers.
        self.waiter="John"

    # Define the menu function which will welcome the customer and present the menu.
    def menu(self):
        # Welcome the customer.
        print("Welcome {}. Thank you for visiting Breakfast at Monty's. My name is {} and I will be your waiter for today. \nOn the Menu today we have:".format(self.customer,self.waiter))
        # Print all the menu items in a nice format.
        for foods in self.items:
            print("--> " + foods)

    #  Create the ordering function
    def order(self):
        # Create an empty list which the customer items can be added to.
        order_list = []
        # ask the user what the want and capitalise so it matches menu syntax.
        self.order = input("What would you like to order?  ").capitalize()

        # If the order is not in the menu, the customer will be asked to re-input.
        while self.order not in self.items:
            self.order = input("Uh oh, that is not an item on our menu. Please try again  ").capitalize()

        # Otherwise, the item can be added to the order list
        else:
            order_list.append(self.order)
            # Confirmation and customer asked if they would like anything else
            more=input("You have selected {}. Anything else? (y/n) ".format(order_list[0]))
            # If reply is no, process ends
            if more.lower() =="n":
                return "Thank you, your food will be with you shortly."
            # Otherwise, customer is asked what they would like
            else:
                 item2=input("What would you like?  ").capitalize()
                 # If the item is not on the menu, customer asked to re-input.
                 while item2 not in self.items:
                     return input("Uh oh, that is not an item on our menu. Please try again  ").capitalize()
                 # Otherwise, the item can be added to the order list.
                 else:
                    order_list.append(item2)
                    # Customer presented with their order and asked if they want anything else.
                    more2=input("You have chosen {} and {}. Anything else? (y/n) ".format(order_list[0],order_list[1]))
                    if more2.lower() =="n":
                         return "Thank you, your food will be with you shortly."
                    else:
                        # Process repeated for a third item.
                         item3=input("What would you like?  ").capitalize()
                         while item3 not in self.items:
                             return input("Uh oh, that is not an item on our menu. Please try again  ").capitalize()
                         else:
                            order_list.append(item3)
                            return "You have chosen {}, {}, and {}. Thank you, your food will be with you shortly.".format(order_list[0], order_list[1], order_list[2])









