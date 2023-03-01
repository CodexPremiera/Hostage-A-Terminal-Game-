# MODULES
import random


# FUNCTIONS
def probability(rate=0):
    rate = rate/10
    return random.randint(0,10) < rate


# CLASSES
class Victim:
    def __init__(self, name, is_hostaged=True, is_alive=True):
        self.name = name
        self.is_hostaged = is_hostaged
        self.is_alive = is_alive

    # METHODS
    def got_released(self):
        self.is_hostaged = False
        print(f"{self.name} is released.")

    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} is killed.")

    def got_saved(self):
        self.is_hostaged = False
        print(f"{self.name} is saved.")


class Kidnapper:
    def __init__(self, name):
        self.name = name
        self.mercy = 0
        self.is_doing_hostage = True
        self.is_alive = True
        self.is_tackled = False

    # METHODS
    def less_mercy(self):
        print(f"{self.name} got less mercy.")
        self.mercy -= 20


    def releases_victim(self):
        print(f"{self.name} released the victim.")
        victim.got_released()
        self.is_doing_hostage = False

    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} is killed.")

    def got_tackled(self):
        self.is_tackled = True
        print(f"{self.name} is tackled.")

    def shoots_victim(self):
        print(f"{self.name} shoots victim.")
        victim.got_killed()
        sniper.shoots_kidnapper()

    def shoots_player(self):
        print(f"{self.name} shoots {player.name}.")
        player.got_killed()

    def shoots_self(self):
        print(f"{self.name} shoots himself.")
        self.got_killed()


class Player:
    def __init__(self, name):
        self.name = name
        self.has_gun = True
        self.is_alive = True
        self.distance = 2

    # METHODS
    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} got killed.")

    def shoots_kidnapper(self):
        print(f"{self.name} shot the kidnapper.")
        kidnapper.got_killed()
        victim.got_saved()

    def tackled_kidnapper(self):
        print(f"{self.name} tackled the kidnapper.")
        # kills player or himself

    def failed_to_tackle_kidnapper(self):
        print(f"{self.name} failed to tackle the kidnapper.")
        kidnapper.shoots_player()
        kidnapper.shoots_victim()

    def rushes_kidnapper(self):
        if self.distance > 4:
            print("You are too far. Can't rush to the Kidnapper")
            # kidnapper.let_decide()
        else:
            print("You rushed the Kidnapper.")
            kidnapper.less_mercy()
            self.attempts_tackle_kidnapper()

    def attempts_tackle_kidnapper(self):
        # establish the probability based distance
        chance = 0
        if self.distance <= 1:
            chance = 80
        elif 1 < self.distance < 3:
            chance = 100 * ((4-self.distance) / 4)
            chance = int(chance)
        else:
            chance = 20

        # use probability to determine tackle success
        if probability(chance):
            self.tackled_kidnapper()
        else:
            self.failed_to_tackle_kidnapper()

    def misses_shot(self):
        print(f"{self.name} missed shot on the kidnapper.")
        kidnapper.shoots_player()
        kidnapper.shoots_victim()


class Sniper:
    def __init__(self, name):
        self.name = name

    # METHODS
    def shoots_kidnapper(self):
        print(f"{self.name} shoots kidnapper.")
        kidnapper.got_killed()


# OBJECT DECLARATION
kidnapper = Kidnapper('The Kidnapper')
victim = Victim('Annie')
player = Player('You')
sniper = Sniper('The Sniper')

player.rushes_kidnapper()
