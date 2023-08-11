from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print('Concrete Method')
class Child(Father):
    def disp(self):
        print("Child Class")
        print("defining abstractt class")
c=Child()
c.disp()
c.show()