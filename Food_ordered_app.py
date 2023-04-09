class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        
class Admin:
    def __init__(self):
        self.menu = {}
        self.current_id = 1
        
    def add_food_item(self, food_item):
        food_item.food_id = self.current_id
        self.menu[self.current_id] = food_item
        self.current_id += 1
    
    def edit_food_item(self, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        food_item = self.menu.get(food_id)
        if not food_item:
            print("Food item not found.")
            return
        if name:
            food_item.name = name
        if quantity:
            food_item.quantity = quantity
        if price:
            food_item.price = price
        if discount:
            food_item.discount = discount
        if stock:
            food_item.stock = stock
    
    def view_menu(self):
        for food_id, food_item in self.menu.items():
            print(f"ID: {food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")
    
    def remove_food_item(self, food_id):
        if food_id in self.menu:
            del self.menu[food_id]
        else:
            print("Food item not found.")


menu = Admin()

menu.add_food_item(FoodItem("Tandoori Chicken", "5 pieces", 340, 0, 50))
menu.add_food_item(FoodItem("Vegan Burger", "2 piece", 310, 10, 25))
menu.add_food_item(FoodItem("Truffle Cake", "600gm", 950, 5, 10))

menu.view_menu()

menu.edit_food_item(1, price=260, stock=60)

menu.view_menu()

menu.remove_food_item(2)

menu.view_menu()


 

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Admin:
    def __init__(self):
        self.users = []

    def register_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None  

    def show_menu(self):
        print("Menu:")
        print("1. Tandoori Chicken (5 pieces) [INR 340]")
        print("2. Vegan Burger (2 Piece) [INR 310]")
        print("3. Truffle Cake (600gm) [INR 950]")

    def place_order(self, user, item_numbers):
        items = []
        for number in item_numbers:
            if number == 1:
                items.append("Tandoori Chicken (5 pieces) [INR 340]")
            elif number == 2:
                items.append("Vegan Burger (2 Piece) [INR 310]")
            elif number == 3:
                items.append("Truffle Cake (600gm) [INR 950]")
        order = {"user": user.full_name, "items": items}
        user.orders.append(order)

    def view_order_history(self, user):
        print("Order History:")
        for index, order in enumerate(user.orders):
            print(f"{index + 1}. {order['user']}: {', '.join(order['items'])}")

    def update_profile(self, user, full_name, phone_number, email, address, password):
        user.full_name = full_name
        user.phone_number = phone_number
        user.email = email
        user.address = address
        user.password = password

restaurant = Admin()

restaurant.register_user("Shaikh waseem", "1234567890", "skwashu@com", "123 Main St, Anytown, INDIA", "password123")

user = restaurant.login_user("skwashu@com", "password123")

restaurant.show_menu()

restaurant.place_order(user, [2, 3])

restaurant.view_order_history(user)

restaurant.update_profile(user, "Shaikh waseem", "0987654321", "skwashu@com", "450 Second St, Othertown, INDIA", "newpassword450")