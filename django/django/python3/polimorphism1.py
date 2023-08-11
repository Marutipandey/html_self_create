"""def hello(a,b,c=1):
    return a+b+c
print(hello(8,9))
print(hello(8,8,8))"""

class uk():
    def ho(self):
        print("india is a beautiful country")
    def hoo(self):
        print(" beautiful country")
class america():
    def ho(self):
        print("america is a not any country")
    def hoo(self):
        print("country")
apple=uk()
apple.ho()
apple.hoo()
print()

ame=america()
ame.ho()
ame.hoo()
print()


for country in (apple,ame):
    country.ho()
    country.hoo()



