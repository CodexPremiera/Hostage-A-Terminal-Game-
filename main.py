
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
    def __init__(self, name, is_doing_hostage=True, is_armed=True, is_alive=True, is_tackled=False):
        self.name = name
        self.is_doing_hostage = is_doing_hostage
        self.is_alive = is_alive
        self.is_tackled = is_tackled

    # METHODS
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

    def shoots_player(self):
        print(f"{self.name} shoots {player.name}.")
        player.got_killed()

    def shoots_self(self):
        print(f"{self.name} shoots himself.")
        self.got_killed()


class Player:
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive

    # METHODS
    def got_killed(self):
        self.is_alive = False
        print(f"{self.name} got killed.")

    def shoots_kidnapper(self):
        print(f"{self.name} shot the kidnapper.")
        kidnapper.got_killed()
        victim.got_saved()

    def tackles_kidnapper(self):
        print(f"{self.name} tackled the kidnapper.")
        kidnapper.got_tackled()
        victim.got_released()

    def misses_shot(self):
        print(f"{self.name} missed shot on the kidnapper.")
        kidnapper.shoots_player()
        kidnapper.shoots_victim()
        sniper.shoots_kidnapper()


class Sniper:
    def __init__(self, name):
        self.name = name

    # METHODS
    def shoots_kidnapper(self):
        print(f"{self.name} shoots kidnapper.")
        kidnapper.got_killed()


# OBJECT DECLARATION
kidnapper = Kidnapper('Kidnapper')
victim = Victim('Annie')
player = Player('You')
sniper = Sniper('The Sniper')


