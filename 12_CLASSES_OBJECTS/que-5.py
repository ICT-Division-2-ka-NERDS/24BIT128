class Time():
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.sec = seconds
        self.min = minutes
        self.hr = hours
    
    def __add__(self, d1):
        s = (self.sec + d1.sec) % 60
        m = (self.min + d1.min + (self.sec + d1.sec) // 60) % 60
        h = self.hr + d1.hr + (self.min + d1.min + (self.sec + d1.sec) // 60) // 60
        return Time(h, m ,s)
    
    def display(self):
        print(f"Time : {self.hr} Hour/s {self.min} Minute/s {self.sec} Second/s")
    
t1 = Time(2,40,32)
t2 = Time(1,37,58)
t1.display()
t2.display()
t1.__add__(t2).display()