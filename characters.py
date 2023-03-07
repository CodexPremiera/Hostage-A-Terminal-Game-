# MODULES
import random


# FUNCTIONS
def probability(rate=0):
    rate = rate / 10
    return random.randint(0, 10) < rate


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
        self.mercy = 50
        self.is_doing_hostage = True
        self.is_alive = True
        self.is_tackled = False

    # METHODS
    def less_mercy(self):
        print(f"{self.name} got less mercy.")
        self.mercy -= 10

    def plus_mercy(self):
        print(f"{self.name} got more mercy.")
        self.mercy += 10

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

    # Decisive Actions
    def shoot_self_or_player(self):
        # establish the probability based distance
        factor = self.mercy
        if factor >= 50:
            chance = 80
        else:
            chance = 20

        # use probability to determine tackle success
        if probability(chance):
            self.shoots_player()
            sniper.shoots_kidnapper()
        else:
            self.shoots_self()

    def decide_victim_fate(self):
        # establish the probability based on mercy
        factor = self.mercy
        if factor >= 40:
            chance = 80
        else:
            chance = 20

        # use probability to determine victim release or kill
        if probability(chance):
            self.releases_victim()
            self.shoot_self_or_player()
        else:
            self.shoots_player()
            self.shoots_victim()


class Player:
    def __init__(self, name):
        self.name = name
        self.has_gun = True
        self.is_alive = True
        self.distance = 20

    # METHODS
    def enter_name(self):
        self.name = input("-----\nEnter your name to begin game: ")
        input(f"Hello! {self.name}.\n")

    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} got killed.")

    def shoots_kidnapper(self):
        print(f"{self.name} shot the kidnapper.")
        kidnapper.got_killed()
        victim.got_saved()

    def pointed_gun_kidnapper(self):
        print(f"{self.name} pointed the gun to the kidnapper.")
        kidnapper.mercy -= 10
        print(f'{self.name} (to the kidnapper): "Drop your gun and release the hostage! Else, I will shoot you!"')

    # Rush Actions
    def tackled_kidnapper(self):
        print(f"{self.name} tackled the kidnapper.")
        kidnapper.shoot_self_or_player()

    def failed_to_tackle_kidnapper(self):
        print(f"{self.name} failed to tackle the kidnapper.")
        kidnapper.shoots_player()
        kidnapper.shoots_victim()

    def attempts_tackle_kidnapper(self):
        # establish the probability based distance
        factor = self.distance
        if factor <= 1:
            chance = 80
        elif 1 < factor < 3:
            chance = 100 * ((4 - factor) / 4)
            chance = int(chance)
        else:
            chance = 20

        # use probability to determine tackle success
        if probability(chance):
            self.tackled_kidnapper()
        else:
            self.failed_to_tackle_kidnapper()

    def rush_kidnapper(self):
        if self.distance > 4:
            print("You are too far. Can't rush to the Kidnapper")
            kidnapper.decide_victim_fate()
        else:
            print("You rushed to the Kidnapper.")
            kidnapper.less_mercy()
            self.attempts_tackle_kidnapper()

    def decide_to_rush(self):
        # ask player whether to rush kidnapper or not
        decision = input("Rush towards the kidnapper and save the victim? (Y/N) ")
        decision = decision.upper()
        while not ((decision == 'Y') or (decision == 'N')):
            decision = input("Please try again. Valid inputs are only 'Y' or 'N': ")
            decision = decision.upper()
        # proceed to rust or not based on player decision
        if decision == 'Y':
            self.rush_kidnapper()
        else:
            kidnapper.decide_victim_fate()

    # Shoot-out Actions
    def misses_shot(self):
        print(f"{self.name} missed shot on the kidnapper.")
        kidnapper.shoots_player()
        kidnapper.shoots_victim()

    def execute_kidnapper(self):
        # establish the probability based distance
        factor = self.distance
        if factor <= 5:
            chance = 80
        elif 5 < factor < 15:
            chance = 100 * ((4 - factor) / 4)
            chance = int(chance)
        else:
            chance = 20
        # use probability to determine execution success
        if probability(chance):
            self.shoots_kidnapper()
        else:
            self.misses_shot()

    def decide_to_execute_or_intimidate(self):
        # ask player whether to execute or intimidate kidnapper
        decision = input("Execute or intimidate kidnapper? (Y/N) ")
        decision = decision.upper()
        while not ((decision == 'Y') or (decision == 'N')):
            decision = input("Please try again. Valid inputs are only 'Y' or 'N': ")
            decision = decision.upper()
        # proceed to execute or not based on player decision
        if decision == 'Y':
            self.execute_kidnapper()
        else:
            self.pointed_gun_kidnapper()
            self.decide_to_execute_or_passive()

    def decide_to_execute_or_passive(self):
        # ask player whether to execute kidnapper or let kidnapper decide
        decision = input("Execute kidnapper or let him decide the victim's fate? (Y/N) ")
        decision = decision.upper()
        while not ((decision == 'Y') or (decision == 'N')):
            decision = input("Please try again. Valid inputs are only 'Y' or 'N': ")
            decision = decision.upper()
        # proceed to execute or alternatively based on player decision
        if decision == 'Y':
            self.execute_kidnapper()
        else:
            kidnapper.decide_victim_fate()

    def decide_to_use_gun(self):
        # ask player whether to use gun or not
        if not self.has_gun:
            return
        decision = input("Use your gun? (Y/N) ")
        decision = decision.upper()
        while not ((decision == 'Y') or (decision == 'N')):
            decision = input("Please try again. Valid inputs are only 'Y' or 'N': ")
            decision = decision.upper()
        # proceed to use gun or not
        if decision == 'Y':
            self.decide_to_execute_or_intimidate()
        else:
            self.decide_to_rush()


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
