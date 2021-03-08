from abc import abstractmethod, ABCMeta

# 创建一个抽象类
class AbstractCustomer(metaclass = ABCMeta):
    name = ""
    @abstractmethod
    def isNil(self):
        pass
    @abstractmethod 
    def getName(self): 
        pass
# 创建扩展了AbstractCustomer的实体类
class RealCustomer(AbstractCustomer):
    def __init__(self, inName):
        self.name = inName
    def getName(self):
        return self.name
    def isNil(self):
        return Falseclass NullCustomer(AbstractCustomer):
    def getName(self):
        return "Not Available in Customer Database"
    def isNil(self):
        return True

# 创建CustomerFactory类
class CustomerFactory():
    names = ["Rob", "Joe", "Julie"]
    @staticmethod
    def getCustomer(inName):
        for aName in CustomerFactory.names:
            if aName.upper() == inName.upper():
                return RealCustomer(inName)
        return NullCustomer()# 调用输出
if __name__ == '__main__':
    customer1 = CustomerFactory.getCustomer("Rob")
    customer2 = CustomerFactory.getCustomer("Bob")
    customer3 = CustomerFactory.getCustomer("Julie")
    customer4 = CustomerFactory.getCustomer("Laura")
    print("Customers")
    print(customer1.getName())
    print(customer2.getName())
    print(customer3.getName())
    print(customer4.getName())