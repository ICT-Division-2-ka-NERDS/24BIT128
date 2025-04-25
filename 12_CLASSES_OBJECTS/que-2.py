class Matrix():
    def __init__(self,data):
        self.data = data
        self.r = len(data)
        self.c = len(data[0])
    
    def __add__(self,m2):
        m3 = Matrix([[self.data[i][j] + m2.data[i][j] for j in range(self.c)] for i in range(self.r)])
        return m3
    
    def multiplication(self,m2):
        m3 = Matrix([[(self.data[i][j] * m2.data[j][i]) for j in range(self.c) ] for i in range(self.r)])
        return m3
    
    def transpose(self):
        m3 = Matrix([[self.data[j][i] for j in range(self.c)] for i in range(self.r)])
        return m3
        
    def display(self):
        for ele in self.data:
            print(ele)
        print("\n")

m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,6,3],[8,5,2],[7,4,1]])
m1.display()
m2.display()
m1.__add__(m2).display()
m1.multiplication(m2).display()
m1.transpose().display()