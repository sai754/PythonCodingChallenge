from Interface.OrderManagementRepo import IOrderManagementRepository
from Util.DBConn import DBConnection
from Entity.user import User
from Exception.OrderProccessorExce import OrderNotFound,UserNotFound
class OrderProcessor(IOrderManagementRepository,DBConnection):
    def getUserRole(self,username):
        try:
            self.cursor.execute("SELECT role FROM Users WHERE username = ?", username)
            row = self.cursor.fetchone()
            if row:
                return row[0] 
            else:
                return "User not found"
        except Exception as e:
            print("Error getting user role:", e)
            return None
    def createProduct(self, user, product):
        try:
            self.cursor.execute("INSERT INTO Products (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                                product.getProductId(), product.getProductName(), product.getDescription(), product.getPrice(), product.getQuantityInStock(), product.getType())
            if product.getType() == "Electronics":
                Brand = (input("Enter the Brand Name: "))
                warranty = int(input("Enter the Warranty Period"))
                self.cursor.execute("INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES (?, ?, ?)",
                                    product.getProductId(), Brand, warranty)
            elif product.getType() == "Clothing":
                size = input("Enter the size of the clothing (M,L,XL,S): ")
                color = input("Enter the color of the clothing: ")
                self.cursor.execute("INSERT INTO Clothing (productId, size, color) VALUES (?, ?, ?)",
                                    product.getProductId(), size, color)
            self.conn.commit()
            print("Product created successfully.")
        except Exception as e:
            print("Error creating product:", e)

    def getAllProduct(self):
        self.cursor.execute("Select * from Products")
        for row in self.cursor:
            print(row)
    
    def getUser(self,username):
        try:
            self.cursor.execute("SELECT username FROM Users WHERE username = ?", username)
            row = self.cursor.fetchone()
            if row:
                return row[0] 
            else:
                return None
        except Exception as e:
            print("Error getting user role:", e)
            return None
    
    def createUser(self, user):
        try:
            self.cursor.execute("INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                                user.getUserId(), user.getUsername(), user.getPassword(), user.getRole())
            self.connection.commit()
            print("User created successfully.")
        except Exception as e:
            print("Error creating user:", e)
    
    def createOrder(self, user, products):
        try:
            self.cursor.execute("INSERT INTO orders (userId) VALUES (?)", user.getUserId())
            self.conn.commit()
            self.cursor.execute("SELECT TOP 1 orderId FROM orders ORDER BY orderId DESC")
            orderId = self.cursor.fetchone()[0]
            for product_id in products:
                qn = int(input(f"Enter the quantity for orderid {product_id}: "))
                self.cursor.execute("INSERT INTO OrderDetails (orderId, productId, quantity) VALUES (?, ?, ?)",
                                    orderId, product_id, qn)  
            self.conn.commit()
            print("Order created successfully.")
        except Exception as e:
            print("Error creating order:", e)

    def getUserbyUsername(self,username):
        self.cursor.execute("Select * from Users where username = ?",username)
        row = self.cursor.fetchone()
        user = User(row.userId, row.username, row.password, row.role)
        return user
    
    def cancelOrder(self, userId, orderId):
        try:
        
            self.cursor.execute("SELECT * FROM Users WHERE userId = ?", userId)
            user_row = self.cursor.fetchone()
            if not user_row:
                raise UserNotFound(f"User with ID {userId} not found.")

            self.cursor.execute("SELECT * FROM orders WHERE orderId = ?", orderId)
            order_row = self.cursor.fetchone()
            if not order_row:
                raise OrderNotFound(f"Order with ID {orderId} not found.")

            
            self.cursor.execute("DELETE FROM OrderDetails WHERE orderId = ?", orderId)
            self.cursor.execute("DELETE FROM orders WHERE orderId = ?", orderId)
            self.conn.commit()
            print("Order canceled successfully.")
        except UserNotFound as e:
            print(e)
        except OrderNotFound as e:
            print(e)
        except Exception as e:
            print("Error canceling order:", e)
    
    def getOrderByUser(self,user):
        self.cursor.execute("""SELECT o.orderId, od.productId, p.productName, od.quantity FROM Orders o \
                                INNER JOIN OrderDetails od ON o.orderId = od.orderId \
                                INNER JOIN Products p ON od.productId = p.productId \
                                WHERE o.userId = ?""", user.userId)
        for row in self.cursor:
            print(row)