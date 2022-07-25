import random as r

class Fash:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print("我的位置是：",self.x,self.y)

class Godfash(Fash):
    pass
class Gapfash(Fash):
    pass
class Bifash(Fash):
    pass
class Dogfash(Fash):
    def __init__(self):
        self.hugry = True
    def eat(self):
        if self.hugry:
            print("鱼的梦想天天吃：")
            self.hugry = False
        else:
            print("吃不下了")