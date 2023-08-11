class ho:
    def __init__(self):
        self.va=10
        self.__speed_limit=20   #double underscore se vo value change nahi hota hai ,it is a privatte memkber so encap value is not change
    def hp(self):
        return self.va
    def hs(self):
        return self.__speed_limit
s=ho()
s.va=100
s.__speed_limit=50  #not change value ,new ffunction banake usake thru change kar denge
print(s.hp(),s.hs())
