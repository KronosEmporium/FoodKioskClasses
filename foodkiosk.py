# Food Kiosk Classes and Methods
#
# Example classes and methods for an automated food kiosk
# ordering system. Items from a database would be added to
# an order which would then be used to create a receipt.
# 
# Possible extensions to this script would be a class or
# database of modifiers that would affect the price of an
# order per OrderItem.
#
# By Crosby Allison 2019

import datetime

class MenuItem:

  # Base class for an item.
  def __init__(self, id, price, name, desc):
    self.__menuItemID = id
    self.__menuItemPrice = price
    self.__menuItemName = name
    self.__menuItemDescription = desc

  # Gets the Menu Item ID.
  def getMenuItemID(self):
    return self.__menuItemID

  # Sets the Menu Item ID.
  def setMenuItemID(self, id):
    self.__menuItemID = id

  # Gets the Menu Item price.
  def getMenuItemPrice(self):
    return self.__menuItemPrice

  # Sets the Menu Item price.
  def setMenuItemPrice(self, price):
    self.__menuItemPrice = price
  
  # Gets the Menu Item name.
  def getMenuItemName(self):
    return self.__menuItemName

  # Sets the Menu Item name.
  def setMenuItemName(self, name):
    self.__menuItemName = name

  # Gets the Menu Item description.
  def getMenuItemDescription(self):
    return self.__menuItemDescription

  # Sets the Menu Item description.
  def setMenuItemDescription(self, desc):
    self.__menuItemDescription = desc

class OrderItem(MenuItem):
  
  # The Order Item inherits all variables and methods belonging to the Menu Item class. The Order Item has an additional ID variable and Modifications variable.

  def __init__(self, id, mid, price, name, desc, mods):
    MenuItem.__init__(self, mid, price, name, desc)
    self.__orderItemID = id
    self.__orderItemModifications = mods

  # Gets the Order Item ID.
  def getOrderItemID(self):
    return self.__orderItemID

  # Sets the Order Item ID.
  def setOrderItemID(self, id):
    self.__orderItemID = id

  # Gets the Order Item Modifications.
  def getOrderModifications(self):
    return self.__orderItemModifications

  # Sets the Order Item Modifications.
  def setOrderModifications(self, mods):
    self.__orderItemModifications = mods

class Order:
  def __init__(self, id, details):
    self.__orderID = id
    self.__orderItems = []
    self.__ordertime = 0
    self.__orderDetails = details
    self.__orderTotal = 0

    # By default, the order time is set when the Order is instantiated. Use self.setOrderTime to override.
    self.setOrderTime(datetime.datetime.now())

  # Gets the Order ID.
  def getOrderID(self):
    return self.__orderID

  # Sets the Order ID.
  def setOrderID(self, id):
    self.__orderID = id

  # Gets the Order Items. Instead of setOrderItems(), items are added through addItem(), removeItem(), and clearOrderItems()
  def getOrderItems(self):
    return self.__orderItems

  # Adds an OrderItem to the Order's list of OrderItems.
  # (only if the type of the item is OrderItem)
  def addOrderItem(self, item):
    if(type(item).__name__ == "OrderItem" or item.__class__.__name__ == "OrderItem"):
      self.__orderItems.append(item)

      # Update order total.
      self.setOrderTotal()

    else:
      print("The item you are trying to add is not a valid OrderItem.")

  # Removes an OrderItem from the Order's list of OrderItems.
  # (only if the type of the item is OrderItem)
  def removeOrderItem(self, item):
    if(type(item).__name__ == "OrderItem" or item.__class__.__name__ == "OrderItem"):
      self.__orderItems.remove(item)

      # Update order total.
      self.setOrderTotal()

    else:
      print("The item you are trying to remove is not a valid OrderItem.")

  def clearOrderItems(self):
    self.__orderItems = []

  # Gets the Order time.
  def getOrderTime(self):
    return self.__ordertime

  # Sets the Order time.
  def setOrderTime(self, time):
    self.__ordertime = time

  # Gets the Order details.
  def getOrderDetails(self):
    return self.__orderdetails

  # Sets the Order details.
  def setOrderDetails(self, details):
    self.__orderdetails = time
  
  # Gets the Order total.
  def getOrderTotal(self):
    return self.__orderTotal

  # Adds the prices of each OrderItem, then sets the Order total to the result.
  def setOrderTotal(self):
    _orderItemPrices = [x.getMenuItemPrice() for x in self.getOrderItems()]
    self.__orderTotal = sum(_orderItemPrices)

class Receipt:
  def __init__(self, id, cname, order, msg):
    self.__receiptID = id
    self.__cashierName = cname
    self.__order = order
    self.__receiptMessage = msg

  # Gets the Receipt ID.
  def getReceiptID(self):
    return self.__receiptID

  # Sets the Receipt ID.
  def setReceiptID(self, id):
    self.__receiptID = id

  # Gets the Cashier name.
  def getCashierName(self):
    return self.__cashierName

  # Sets the Cashier name.
  def setCashierName(self, name):
    self.__cashierName = name

  # Gets the Order for this receipt.
  def getOrder(self):
    return self.__order

  # Sets the Order for this receipt.
  def setOrder(self, order):
    self.__order = order

  # Gets the Receipt message.
  def getReceiptMessage(self):
    return self.__receiptMessage

  # Sets the Receipt message.
  def setReceiptMessage(self, msg):
    self.__receiptMessage = msg


# Tests
item1 = MenuItem(0, 10, "Regular Burger", "A really tasty burger.")
item2 = MenuItem(1, 11, "Irregular Burger", "An even tastier burger.")

oitem1 = OrderItem(0, item1.getMenuItemID(), item1.getMenuItemPrice(), item1.getMenuItemName(), item1.getMenuItemDescription(), "no cheese")
oitem2 = OrderItem(2, item2.getMenuItemID(), item2.getMenuItemPrice(), item2.getMenuItemName(), item2.getMenuItemDescription(), "extra cheese")

order1 = Order(0, "Order 1")
order1.addOrderItem(oitem1)
order1.addOrderItem(oitem2)

# Make a receipt with ID 0, cashier "Doug", order = order1, message "Have a great day!". Prints mock receipt.
receipt1 = Receipt(0, "Doug", order1, "Have a great day!")
print("""Thank you for dining with us.
Receipt No.: %d
Cashier: %s

Items:
%s

Order Total: $%.2f
%s""" % (receipt1.getReceiptID(), receipt1.getCashierName(), "\n".join([x.getMenuItemName() + (" $%.2f" % x.getMenuItemPrice()) for x in receipt1.getOrder().getOrderItems()]), receipt1.getOrder().getOrderTotal(), receipt1.getReceiptMessage()))
