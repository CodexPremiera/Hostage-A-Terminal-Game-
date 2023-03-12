# IMPORT MODULE
from textwrap import dedent
import time
import characters

# CHARACTERS
player = characters.player
victim = characters.victim
kidnapper = characters.kidnapper
sniper = characters.sniper

# VARIABLES
set_time = 0


# TASK FUNCTIONS
def press_continue(prompt="enter to continue_"):
    input(f">>> {prompt}")
    print("")


def ask_char(prompt_str, choice_list):
    inp = ''
    while inp not in choice_list:
        inp = input(f">>> {prompt_str}")
        inp = inp.upper()
    return inp


def ask_int(prompt_str, choice_list):
    choice = -2.718
    while choice not in choice_list:                    # Check if the input is within the choices
        choice = input(f">>> {prompt_str}")
        try:
            choice = int(choice)                        # Check if the input is of a valid type
        except ValueError:
            continue
    value = choice
    return value


def print_stats(stat_list):
    stats = "\n--------------------"
    for stat in stat_list:
        stats += f"\n{stat}"
    stats += "\n--------------------"
    print(f"{stats}")


# SCRIPT FUNCTIONS
def print_title():
    text = f"""
        ##### #####  ###   ###  ##### #####  ###  #####    #   #  ###   ###  #####  ###   ###  #####   
        # # #   #   #     #       #     #   #   # #   #    #   # #   # #       #   #   # #     #
        # # #   #    ###   ###    #     #   #   # #   #    ##### #   #  ###    #   ##### #  ## #####
        # # #   #       #     #   #     #   #   # #   #    #   # #   #     #   #   #   # #   # #
        # # # #####  ###   ###  ##### #####  ###  #   #    #   #  ###   ###    #   #   #  ###  #####
        --------------------------------------------------------------------------------------------
        WELCOME TO THE MISSION HOSTAGE GAME 
        --------------------------------------------------------------------------------------------
        """
    print(f"{dedent(text)}")
    press_continue()


def print_overview():
    text = """
        -----
        One late evening, you arrive at an office at the top floor of a high rise residential building.
        The police approached you.
        """
    print(f"{dedent(text)}")


def talk_with_police():
    script = {
        'POL_0': """        👮‍ POLICE OFFICER
                Good evening sir! I would like to brief you about the situation.
                """,
        'YOU_0': """        🤵️ NEGOTIATOR (YOU)
                The way I see it, it is not so good of an evening. Anyways, I'm all ears.
                """,
        'POL_1': """        👮‍♂️ POLICE OFFICER 
                There is a hostage situation happening at the outdoor lounge at the rooftop of this 
                building. A man is holding his girlfriend at gunpoint. We already have the snipers in 
                position. However, we can't risk shooting the man. If we miss, the girl can get shot.
                """,
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Do you know his motives?
                """,
        'POL_2': """        👮‍♂️ POLICE OFFICER 
                We have no clue sir. But we did find a dead man in their room. Apparently, he was shot.
                We suspect this has something to do about their relationship.
                """,
        'YOU_2': """        🤵 NEGOTIATOR (YOU)
                That's unfortunate. It seems the man is really twisted right now.
                """,
        'POL_3': """        👮‍♂️ POLICE OFFICER
                I agree sir. But we still need to save the girl at all cost.
                """,
        'YOU_3': """        🤵️ NEGOTIATOR (YOU)
                I know. Do you have their names?
                """,
        'POL_4': """        👮‍♂️ POLICE OFFICER
                Yes sir, the man's name is Berthold, and the girl's is Annie.   
                """,
        'YOU_4': """        🤵 NEGOTIATOR (YOU)
                That is all I need. Thank you.
                """
    }
    for values in script.values():
        print(f"{values}")
        time.sleep(set_time)
    press_continue()


def print_mission():
    text = f"""\
        --------------------------------------------------------------------------------------------
        MISSION: 
         ▶ Talk with Berthold and gain his trust. 
         ▶ Save the girl at all cost.
         
         {player.print_distance()}
         {kidnapper.print_trust()}
        --------------------------------------------------------------------------------------------
        """
    print(f"{dedent(text)}")
    press_continue()


def initial_encounter():
    script_1 = {
        'NAR_0': "-----",
        'NAR_1': """You went outside the office and slowly approached the scene. Berthold, the hostage taker, sees you.
                """,
        'NAR_2': """        BANG! 🔫💨💥\
                """,
        'NAR_3': """        A bullet barely missed you. You stopped on your spot
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                (to you): STAY BACK! Don't come any closer, or I'll shoot her. 
                """,
        'ANN_1': """        👩‍💼 ANNIE
                (afraid and crying)
                (to Berthold): NO Berthold, please! I'm begging you!
                """,
        'ANN_2': """\
                (to You): Please sir. Save me!
                """
    }
    for values in script_1.values():
        print(f"{values}")
        time.sleep(set_time)

    # Decide whether to stop walking or not as Berthold commands
    answer = ask_char("Obey Berthold and stop walking? (Y/N)_", ['Y', 'N'])
    print("---")
    if answer == 'N':
        player.walk_cont(5)
        kidnapper.less_trust()
    else:
        player.walk_stop()
        kidnapper.plus_trust()
    print('')

    # Introduce the player's self to Berthold while walking or staying as decided
    script_2 = {
        'YOU_1': f"""        🤵 NEGOTIATOR (YOU)
                Hello Berthold. My name is {player.name}. I am a trained negotiator. 
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                How... how do you know my name?
                """,
        'YOU_2': """        🤵 NEGOTIATOR (YOU)
                (to you): I know a lot of things about you Berthold. I've come to help you out of this."""
    }
    # Display game stats as a result of decision to walk or not
    for values in script_2.values():
        print(f"{values}")
        time.sleep(set_time)
    info = [player.print_distance(), kidnapper.print_trust()]
    print_stats(info)


def talk_to_kidnapper(instruction_str, options_dict, consider_has_gun=False):
    # Display the instruction and the available action choices
    instruct = ""
    instruct += f"\n{instruction_str}\n"                        # Print instruction header of the act
    options_list = [key for key in options_dict.keys()]         # Make a list of all playable options
    options_nums = [i+1 for i in range(len(options_list))]      # Get the numbers of playable options
    for i in options_nums:
        instruct += f"\t {i} - {options_list[i-1]}\n"
    print(instruct)

    # Let player choose what to say to the Hostage Taker
    inp_num = ask_int("Enter chosen number: ", options_nums)    # Ask player for number of chosen option
    inp_str = options_list.pop(inp_num-1)                       # Remove the chosen option from its list
    print(f"You have chosen to {inp_str.lower()}.")

    # Talk to Hostage Taker with the chosen emotion
    script = options_dict.pop(inp_str)                          # Remove the chosen option its dict
    if script[0] > 0:                                           # Increase kidnapper's trust level
        kidnapper.plus_trust()
    elif script[0] < 0:                                         # Decrease kidnapper's trust level
        kidnapper.less_trust()
    else:
        print(f"{kidnapper.name}'s trust level is unchanged.")  # No change on kidnapper's trust level
    print("")
    for values in script[1].values():                           # Execute the chosen options sequence
        print(f"{values}")
        time.sleep(set_time)
    info_list = [kidnapper.print_trust()]                       # Print kidnapper's trust level after action

    # Additional Task: Has Gun
    if consider_has_gun:
        if script[0] > 0:                                       # Consider player's gun; Drop/keep gun
            player.drop_gun()
        else:
            player.keep_gun()
        info_list.append(player.print_has_gun())                # Print kidnapper's stats after action
    print_stats(info_list)



