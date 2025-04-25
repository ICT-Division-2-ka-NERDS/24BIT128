class Date():
    def __init__(self, date, month, year):
        self.d = date
        self.m = month
        self.y = year
        
    def compare(self, d1):
        if (self.d == d1.d and self.m == d1.m and self.y == d1.y):
            return True
    def display_date(self):
        print(f"d1 : {self.d}/{self.m}/{self.y}")
    
    def display(self, d1):
        if (self.compare(d1)):
            print("Entered both dates are same.")
        else :
            print("Ener both dates aren't same.")
    
d1 = Date(25, 4, 2025)
d2 = Date(25, 4, 2025)
d1.display_date()
d1.display_date()
d1.display(d2)