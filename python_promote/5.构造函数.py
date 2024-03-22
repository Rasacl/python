# 构造函数
# __init__ 具有初始化的作用，放该类被实例化的时候会自动执行该函数
# 注意 类里面没有这个方法__init__() ,python会自动创建，但是不会执行任何操作

class Hero:
    def __init__(self):
        self.name = '泰塔'
        self.hp = 200
        self.at = 450
    def move(self):
        print(f'{self.name}正在移动')

    def attack(self):
        print(f'{self.name}生命值{self.hp},发出了一招攻击{self.at}')

# 创建对象
hero = Hero()
hero.move()
hero.attack()