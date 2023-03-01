player_lives = "Player Lives"
player_dies = "Player Dies"
victim_released = "Victim is released"
victim_killed = "Victim is killed"
hostage_taker_surrenders = "Hostage-taker surrenders and is arrested"
hostage_taker_killed = "Hostage-taker is killed"


class Victim:
    def __init__(self, is_hostaged=True, is_alive=True):
        self.name = "Annie"
        self.is_hostaged = is_hostaged
        self.is_alive = is_alive

    # METHODS
    def released(self):
        self.is_hostaged = False
        print(victim_released)

    def killed(self):
        self.is_alive = False
        print(victim_killed)
