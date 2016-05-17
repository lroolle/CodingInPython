# attack_defender_game.py


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
