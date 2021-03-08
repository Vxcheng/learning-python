# Command Pattern with Python Code
from abc import  abstractmethod,ABCMeta

# 创建一个命令接口Order
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

# 创建一个请求类
class Stock():
    _name = "ABC"
    _quantity = 10
    def buy(self):
        print("Stock [Name : {0}, Quantity: {1}] bought.".format(self._name,self._quantity))
    def sell(self):
        print("Stock [Name : {0}, Quantity: {1}] sold.".format(self._name, self._quantity))

# 创建实现了Order接口的实体类
class BuyStock(Order):
    _abcStock = None
    def __init__(self,inStock):
        self._abcStock = inStock
    def execute(self):
        self._abcStock.buy()
class SellStock(Order):
    _abcStock = None
    def __init__(self,inStock):
        self._abcStock = inStock
    def execute(self):
        self._abcStock.sell()

# 创建命令调用类
class Broker():
    _orderList = []
    def takeOrder(self,inOrder):
        self._orderList.append(inOrder)
    def placeOrders(self):
        for aOrder in self._orderList:
            aOrder.execute()
        self._orderList.clear()

# 调用输出
if __name__ == '__main__':
    abcStock = Stock()
    buyStockOrder = BuyStock(abcStock)
    sellStockOrder = SellStock(abcStock)

    broker = Broker()
    broker.takeOrder(buyStockOrder)
    broker.takeOrder(sellStockOrder)

    broker.placeOrders()