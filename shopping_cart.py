class ShoppingCart:
    # write your code here
    def __init__(self, total = 0, items=[], employee_discount=0):
       self.total = total
       self.items = items
       self.employee_discount = employee_discount

    def add_item(self, name, price, quantity=1):
       item_dict = {'name': name, 'price': price, 'quantity': quantity}
       self.items.append(item_dict)
       self.total += price * quantity
       return self.total

    def mean_item_price(self):
       total_items = 0
       for i in self.items:
          total_items += i['quantity']
       return self.total / total_items

    def median_item_price(self):
       import statistics
       price_list = []
       for i in self.items:
          for q in range(0, i['quantity']):
             price_list.append(i['price'])
       return statistics.median(price_list) 

    def apply_discount(self):
       if self.employee_discount != 0:
          return self.total * ((100 - self.employee_discount)/100)
       else:
          return 'Sorry, no discount to apply'

    def void_last_item(self):
       try:
          self.total -= self.items[-1]['price']
          self.items.pop()
         
       except:
          return 'Sorry, no items are in the cart at this time'