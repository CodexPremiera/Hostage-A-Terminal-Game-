# -------------------- MODULES -------------------- #
import characters
import game

# -------------------- CHARACTERS --------------------#
player = characters.player
victim = characters.victim
kidnapper = characters.kidnapper
sniper = characters.sniper

# -------------------- PLOT -------------------- #


# -------------------- GAME SEQUENCE -------------------- #

game.print_title()
player.enter_name()

game.print_overview()
game.talk_with_police()
game.print_mission()

