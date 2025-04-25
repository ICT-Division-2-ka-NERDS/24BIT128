class Weather():
    def __init__(self, data):
        self.parameters = data
        
    def __contains__(self,data):
        return data in self.parameters
    
w1 = Weather(["windy","sunny","rainy"])
print(w1.__contains__("rainy"))