# Task 2 - Restaurant Waiter 

### Summary
Make a program that helps a waiter with their menu and orders.
### Tasks
1. Format the menu so the user can view 
2. Allow the user to order 3 times and add each response to a list.
3. Repeat order back to user for confirmation. 
### Acceptance Criteria
* Completes required tasks
* Create a new project and repository
* Have at least 5 commits
* Include documentation
* Follow best practices

# Process 
#### 1. Create a Menu class.
 * This is the parent class within which the menu items are defined. 
```python
class Menu:
    def __init__(self):
        # Define the menu items
        self.items=["Pancakes","Waffles","Eggs Benedict","Bagels","Full English","Porridge", "Cake","Cereal"]
```
#### 2. Creation of an Order class 
* This is a child class of the Menu class. 
```python
# Import the menu class
from menu import Menu
# Create the Order class which is a child of Menu
class Order(Menu):
```
* The class is initialised and asks the user for their name so as to personalise the greeting. 
* The init function also defines the waiter name so it can easily be changed if the server changes.
* The super method is used to inherit attribtes from the parent class
```python
    def __init__(self):
        # Inherit parent attributes using super
        super().__init__()
        # Ask the customer for their name, to personalise the experience
        self.customer=input("Please enter your name: ").capitalize()
        # Define waiter/waitress name here so can easily be changed for different servers.
        self.waiter="John"
```


* The menu function prints a welcome statement, utilising inputs collected during the init function. 
* It formats this with the menu inherited from the parent class Menu. 
```python
    # Define the menu function which will welcome the customer and present the menu.
    def menu(self):
        # Welcome the customer.
        print("Welcome {}. Thank you for visiting Breakfast at Monty's. My name is {} and I will be your waiter for today. \nOn the Menu today we have:".format(self.customer,self.waiter))
        # Print all the menu items in a nice format.
        for foods in self.items:
            print("--> " + foods)
```


```python
  #  Create the ordering function
    def order(self):
        # Create an empty list which the customer items can be added to.
        order_list = []
        # ask the user what the want and capitalise so it matches menu syntax.
        self.order = input("What would you like to order?  ").capitalize()

        # If the order is not in the menu, the customer will be asked to re-input.
        while self.order not in self.items:
            self.order = input("Uh oh, that is not an item on our menu. Please try again  ")

        # Otherwise, the item can be added to the order lis
        else:
            order_list.append(self.order)
            # Confirmation and customer asked if they would like anything else
            more=input("You have selected {}. Anything else? (y/n) ".format(order_list[0]))
            # If reply is no, process ends
            if more.lower() =="n":
                return "Thank you, your food will be with you shortly."
            else:
                 item2=input("What would you like?  ")
                 order_list.append(item2)
                 more2=input("You have chosen {} and {}. Anything else? (y/n) ".format(order_list[0],order_list[1]))
                 if more2.lower() =="n":
                     return "Thank you, your food will be with you shortly."
                 else:
                     item3=input("What would you like?  ")
                     order_list.append(item3)
                     print("You have chosen {}, {}, and {}. Thank you, your food will be with you shortly.".format(order_list[0], order_list[1], order_list[2]))
```
 



