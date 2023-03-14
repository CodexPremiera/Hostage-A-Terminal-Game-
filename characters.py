# MODULES
import random


# FUNCTIONS
def probability(rate=0):
    rate = rate / 10
    return random.randint(0, 10) < rate


def press_continue(prompt="enter to continue_"):
    input(f">>> {prompt}")


# CLASSES
class Victim:
    def __init__(self, name, is_hostaged=True, is_alive=True):
        self.name = name
        self.is_hostaged = is_hostaged
        self.is_alive = is_alive

    # METHODS
    def got_released(self):
        self.is_hostaged = False
        print(f"{self.name} is released.\n")

    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} is killed.\n")


class Kidnapper:
    def __init__(self, name):
        self.name = name
        self.trust = 50
        self.is_doing_hostage = True
        self.is_alive = True

    def print_trust(self):
        stats = f"{self.name}'s Mercy Level: {self.trust}%"
        return stats

    # METHODS
    def less_trust(self, trust_change=8):
        self.trust -= trust_change
        if self.trust < 0:
            trust_change -= 0 - self.trust
            self.trust = 0
        print(f"{self.name}'s trust level is reduced by {trust_change}%")

    def plus_trust(self, trust_change=8):
        self.trust += trust_change
        if self.trust > 100:
            trust_change -= 100 - self.trust
            self.trust = 100
        print(f"{self.name}'s trust level is increased by {trust_change}%")

    def releases_victim(self):
        print(f"{self.name} releases {victim.name}.")
        victim.got_released()
        self.is_doing_hostage = False

    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} is killed.")

    def shoots_victim(self):
        print(f"{self.name} shoots victim.")
        victim.got_killed()
        police.shoots_kidnapper()

    def shoots_player(self):
        print(f"{self.name} shoots you.")
        player.got_killed()

    def shoots_self(self):
        print(f"{self.name} shoots himself.")
        self.got_killed()

    def surrenders(self):
        print(f"{self.name} drops his gun and surrenders.")
        police.arrests_kidnapper()


class Player:
    def __init__(self):
        self.name = ""
        self.has_gun = True
        self.is_alive = True
        self.distance = 20

    def print_distance(self):
        stats = f"Your distance to {kidnapper.name}: {self.distance}m"
        return stats

    def print_has_gun(self):
        stats = f"You have a gun: {self.has_gun}"
        return stats

    # METHODS
    def enter_profile(self):
        while self.name == "":
            self.name = input(">>> Enter your name to begin game: ")
        print(f"Greetings, {self.name}! 🤵 \n")
        press_continue()

    def walk_cont(self, distance=4):
        self.distance -= distance
        print("You continue to walk very slowly towards the hostage taker.")
        print(f"Distance to {kidnapper.name} will be reduced by {distance}m")
        kidnapper.less_trust()

    def walk_stop(self, distance=0):
        self.distance -= distance
        print("You stayed in you place for a while.")
        print(f"Distance to {kidnapper.name} is unchanged.")
        kidnapper.plus_trust()

    def keep_gun(self):
        self.has_gun = True
        print("\nSince you kept your gun, you are still armed.")

    def drop_gun(self):
        self.has_gun = False
        print("\nSince you dropped your gun, you are now unarmed.")

    def got_killed(self):
        self.is_alive = False
        print(f"You got killed.\n")


class Police:
    def __init__(self, name):
        self.name = name

    # METHODS
    def shoots_kidnapper(self):
        print(f"{self.name} sniper shoots {kidnapper.name}.")
        kidnapper.got_killed()

    def arrests_kidnapper(self):
        print(f"{self.name} came into the scene and arrests {kidnapper.name}.")


# OBJECT DECLARATION
kidnapper = Kidnapper('Berthold')
victim = Victim('Annie')
player = Player()
police = Police('The Police')
