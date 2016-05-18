"""实现一玩家类，有进攻和格挡 2 种行为，正常、死亡、僵死 3 种状态，上身、下身 2 个攻击位置，
    以及血量。游戏开始时，防守方首先设置格挡位置，然后进攻方进行攻击，双方轮流进行。
    如果进攻方的攻击位置等于防守方的格挡位置，那么不造成伤害。

    如果击中上身，受到 10 点伤害，下身击中，受到 5 点伤害，如果没有设置格挡位置，受到额外 5 点伤害。
    每回合结束后，格挡位置置空。

    一旦血量归 0，则变为死亡状态，死亡状态下再次受到攻击，变为僵尸。
    初始血量均为 30 点。

"""


class GameOver(BaseException):
    pass


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.position = None
        self.state = 1

    def set_block(self, position):
        if self.state == -1:
            raise GameOver
        self.position = position

    def attack(self, goal, position):
        if self.state <= 0:
            return

        if not isinstance(goal, Player):
            raise AttributeError

        if position not in ('low', 'high'):
            raise AttributeError

        if goal.health == 0:
            goal.state = -1
            print(goal.name + ' become a zombie')
            return

        if position == goal.position:
            pass
        elif position == 'high':
            goal.health -= 10
        else:
            goal.health -= 5

        if goal.position is None:
            goal.health -= 5

        if goal.health <= 0:
            goal.state = 0
            goal.health = 0
            print(goal.name + ' is dead')

        print(goal.name + str(goal.health))
        goal.set_block(None)


attacker = Player('小明')
defender = Player('老师')

for i in range(10):
    print('Round ' + str(i + 1))
    defender.set_block('low')
    attacker.attack(defender, 'high')

    attacker.set_block('low')
    defender.attack(attacker, 'high')
