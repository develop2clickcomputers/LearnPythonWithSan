class Calculator:
    def __init__(self):
        pass

    def main(self,   action,  a,  b):
        print("Hello, World! Ready for some math?")
        if action == "add":
            print("The sum of " + str(a) + " and " + str(b) + " is " + str(self.add(a, b)))
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

if __name__ == "__main__":
    calc = Calculator()
    calc.main("add", 5, 3)
