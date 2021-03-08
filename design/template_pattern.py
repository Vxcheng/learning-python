# Template Pattern code with Python
from abc import abstractmethod,ABCMeta

# 创建一个game父类
class Game(metaclass=ABCMeta):

    # 把几乎不变的公共部分代码集中在父亲类，比如showcopyright
    # 此例子中，初始化、开始、结束三个方法，除了游戏名以外，都一样，所以把共性部分放在父类
    def initialize(self):
        print("%s Game Initialized! Start Playing." %self.setGameName())
    def startPlay(self):
        print("%s Game Started. Enjoy the game!" % self.setGameName())
    def endPlay(self):
        print("%s Game Finished! \n" % self.setGameName())
    def play(self):
        self.initialize()
        self.startPlay()
        self.endPlay()

    # 每个游戏子类的抽象部分仅仅是游戏名称的设定
    @abstractmethod
    def setGameName(self):
        pass

class Cricket(Game):
    def setGameName(self):
        return  "Cricket"

class Football(Game):
    def setGameName(self):
        return "Football"

# 调用输出
if __name__ == '__main__':
    game1 = Cricket()
    game1.play()
    game2 = Football()
    game2.play()