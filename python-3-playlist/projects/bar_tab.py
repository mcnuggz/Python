class Tab:
    menu = {
        "Wine": 5.99,
        "Beer": 2.99,
        "Soda_Pop": 1.99,
        "Chicken_Salad": 9.99,
        "Double_Cheeseburger": 11.99,
        "Veggie_Burger": 14.99,
        "Cookies": 2.99
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item] 
    
    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20}${self.menu[item]}')
            
        print(f'{"Tax":20} ${tax:.2f}')
        print(f'{"Total":20} ${total:.2f}')