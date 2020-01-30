# import a


# class b(a.a):
#     def mymethod(self):
#         a.a().method()
#         print("avariable is ", a.avariable)

class one():
    def __init__(self):
        # only self constant in __init__ works 
        self.click = "check me"
        self.click2 = "laksdjfa"
    def method2(self):
        print(self.click + " bobo")
        self.click2 = self.click + " customer support bobo"
    def method3(self):
        print(self.click2)
 
if __name__ == '__main__':
    # print(a.avariable)
    # b().mymethod()
    # b().mymethod()
    print(one().method3())