class String():
    def __init__(self,st):
        self.s = st
    
    def concatenation(self,s1):
        return String(f"{self.s} {s1.s}")
    
    def toLower(self):
        return String(self.s.lower())
    
    def toUpper(self):
        return String(self.s.upper())
    
    def display(self, name):
        print(f"{name} : {self.s}")

s1 = String("Hello")
s2 = String("World")
s1.display("s1")
s2.display("s2")
s3 = s1.concatenation(s2)
s3.display("s1 + s2")
s3.toLower().display("s1 + s2 (in lower)")
s3.toUpper().display("s1 + s2 (in upper)")