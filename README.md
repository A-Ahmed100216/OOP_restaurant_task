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
#### 1. Creation of a Parent class.
 * The Menu class is defined as the parent class within which the menu items are defined. 
```python
class Menu:
    def __init__(self):
        # Define the menu items
        self.items=["Pancakes",
                    "Waffles",
                    "Eggs Benedict",
                    "Bagels",
                    "Full English",
                    "Porridge",
                    "Cake",
                    "Cereal"]
```
#### 2. Creation of a Child class 
* The Order class is a child class of the Menu class therefore the Menu class must be imported.
```python
# Import the menu class
from menu import Menu
# Create the Order class which is a child of Menu
class Order(Menu):
```
* The class is initialised and asks the user for their name so as to personalise the greeting. 
* The init function also defines the waiter name so it can easily be changed if the server changes.
* The super method is used to inherit attributes from the parent class
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

* Create the order function which will be used to take a customers order and repeat back to them.
* An empty list is created to store the customer's order and repeat back to them. 
* The customer is then asked to input what they would like to order. This input is capitalised to match the menu format.  
```python
    def order(self):
        order_list = []
        self.order = input("What would you like to order?  ").capitalize()
```
* If the order is not in the menu, the customer will be asked to try again until they select an item which is on the menu.

```python
        while self.order not in self.items:
            self.order = input("Uh oh, that is not an item on our menu. Please try again  ").capitalize()
```
* If the item is on the menu, it will be added to the empty list.
* The order will be repeated back to the customer and they will be asked if they would like anything else. The customer is directed to respond with y or n. 
```python
        else:      
            order_list.append(self.order)
            more=input("You have selected {}. Anything else? (y/n) ".format(order_list[0]))
```
* If the reply is 'n', the process ends with a simple statement notifying them that their food will be with them shortly.
```python
            if more.lower() =="n":
                return "Thank you, your food will be with you shortly."
```
* Otherwise, the customer can provide a second input, provided it is a menu item. As with the first item, if it is on the menu, it will be appended to the order list and repeated back to the customer. Once again, the customer is asked if they would like anything else and the process repeated. 
```python
                 item2=input("What would you like?  ").capitalize()
                 while item2 not in self.items:
                     return input("Uh oh, that is not an item on our menu. Please try again  ").capitalize()
                 else:
                    order_list.append(item2)
                    
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
```
 
#### 3. Instantiation
* Upon creation of the tasks, a seperate file is created to test the code. 
* The Menu and Order class are both imported. 
```python
from menu import Menu
from order import Order
```
* An instance of the Order class is created. This instance inherits attributes of the Parent class therefore we can use this to display the menu. 
* The order function is called from the Order class and allows customers to input what they would like and view what they have ordered. 
```python
test=Order()
test.menu()
print(test.order())
```

