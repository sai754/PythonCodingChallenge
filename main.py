from DAO import OrderProcessor
from Entity import Clothing, Electronics, Product, User


class OrderManagement:
    
    def mainmenu():
        OrderService = OrderProcessor()
        while(True):
            print("""
    Do you want to:
    1. Create Product
    2. Create Order
    3. Cancel Order
    4. Create User
    5. Get All Products
    6. Get Order By User
    7. Exit""")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                username = input("Enter your username: ")
                role = OrderService.getUserRole(username)
                if role == 'Admin':
                    print("Create A Product")
                    product_id = int(input("Enter the Product id: "))
                    product_name = input("Enter the product name: ")
                    product_description = input("Enter the Product Description: ")
                    pricef = float(input("Enter the price of the product: "))
                    price = "{:.2f}".format(pricef)
                    quantity = int(input("Enter the quantity available: "))
                    type = input("Enter the type (Electronics or Clothing)")
                    if type not in ("Electronics", "Clothing"):
                        print("Enter Valid type")
                    newProduct = Product(product_id,product_name,product_description,price,quantity,type)
                    OrderService.createProduct(username,newProduct)
                else:
                    print("You are not an admin")
            elif choice == 2:
                username = input("Enter your username: ")
                check = OrderService.getUser(username)
                if check == None:
                    print("User Not Available, create user:")
                    userid = int(input("Enter User ID: "))
                    username = input("Enter Username: ")
                    password = input("Enter your Password: ")
                    role = input("Enter your role (Admin or User): ")
                    newUser = User(userid,username,password,role)
                    OrderService.createUser(newUser)
                OrderService.getAllProduct()
                user = OrderService.getUserbyUsername(username)
                product = []
                while True:
                    product_id = int(input("Enter the Product ID (0 to cancel the ordering): "))
                    if product_id == 0:
                        break
                    product.append(product_id)
                OrderService.createOrder(user,product)
            elif choice == 3:
                username = input("Enter your Username: ")
                password = input("Enter your password: ")
                user = OrderService.getUserbyUsername(username)
                if password == user.password:
                    OrderService.getOrderByUser(user)
                    deleteId = int(input("Enter the Order ID you want to Delete: "))
                    ans = input("Are you sure you want to delete the order (yes if you want to): ")
                    if ans == 'yes':
                       OrderService.cancelOrder(user.userId,deleteId) 
                else:
                    print("Invalid Credentials")
            elif choice == 4:
                userid = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter your Password: ")
                role = input("Enter your role (Admin or User): ")
                if role not in ("Admin", "User"):
                    print("Enter a valid role!!")
                newUser = User(userid,username,password,role)
                OrderService.createUser(newUser)
            elif choice == 5:
                OrderService.getAllProduct()
            elif choice == 6:
                username = input("Enter your Username: ")
                user = OrderService.getUserbyUsername(username)
                if user.role != 'Admin':
                    print("You don't have the authorization to check")
                else:
                    OrderService.getOrderByUser(user)
            elif choice == 7:
                print("See you soon")
                OrderService.close()
                break
            else:
                OrderService.close() 
                break
                


if __name__ =='__main__':
    print("Order Management App")
    OrderManagement.mainmenu()
