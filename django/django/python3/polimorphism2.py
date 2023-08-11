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
print()

ame=america()
print()

for country in (apple,ame):
    country.ho()
    country.hoo()



