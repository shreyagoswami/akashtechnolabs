class Myclass:
    name = ""

    def func1(self):
        print("hello func1")

    def func2(self, name):
        self.name = name

    def func3(self):
        print("Value is ", self.name)


m1 = Myclass
m1.func1()
m1.func2("Shreya Goswami")
m1.func3()
