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
    inp = -2.71828
    while inp not in choice_list:
        inp = input(f">>> {prompt_str}")
        inp = int(inp)
    return inp


def print_stats(stat_list):
    stats = "----------"
    for stat in stat_list:
        stats += f"\n{stat}"
    stats += "\n----------"
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
        'YOU_2': """        🤵️ NEGOTIATOR (YOU)
                Any other casualties?
                """,
        'POL_3': """        👮‍♂️ POLICE OFFICER
                Well sir, he has also already killed two of our responding policemen. He also killed two
                civilians and wounded one. That wounded one is currently outside where the hostage is 
                happening. It's a teenage boy. He needs urgent medical attention, but it is too dangerous 
                to approach.
                """,
        'YOU_3': """        🤵 NEGOTIATOR (YOU)
                That's unfortunate. It seems the man is really twisted right now.
                """,
        'POL_4': """        👮‍♂️ POLICE OFFICER
                I agree sir. But we still need to save the girl at all cost.
                """,
        'YOU_4': """        🤵️ NEGOTIATOR (YOU)
                I know. Do you have their names?
                """,
        'POL_5': """        👮‍♂️ POLICE OFFICER
                Yes sir, the man's name is Berthold, and the girl's is Annie.   
                """,
        'YOU_5': """        🤵 NEGOTIATOR (YOU)
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
    else:
        player.walk_stop()
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
                (to you): I know a lot of things about you Berthold. I've come to help you out of this.
                """
    }
    # Display game stats as a result of decision to walk or not
    for values in script_2.values():
        print(f"{values}")
        time.sleep(set_time)
    info = [player.print_distance(), kidnapper.print_trust()]
    print_stats(info)


emotions_dict = {
    'MAKE DEMANDS': [0, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I need you to let her go Berthold. That is the only way this can end.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I am not stupid! I know you are going to shoot me the moment I release her.
                This is how this ends. EITHER I DIE, OR WE BOTH DIE!
                """
        }],
    'TALK THE VICTIM': [0, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                (to Annie): Are you okay Annie?
                """,
        'ANN_1': """        👩‍💼 ANNIE
                (afraid and crying)
                (to You): Please, help me. I don't want to die!
                    """,
        'YOU_2': """        🤵 NEGOTIATOR (YOU)
                (to Annie): Nobody is going to die. Stay calm. Everything is going to be fine.
                """
        }],
    'CALM HIM DOWN': [5, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I need you to calm down, Berthold. Let me help you and everything will be okay.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I don't need your help. Nobody can help me now. JUST LEAVE ME ALONE AND I'LL END THIS.
                """
        }],
    'REASSURE HIM': [5, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I'm not going to hurt you. I just want to talk and find a solution.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                Talk!? I don't want to talk. It's too late for that now. IT'S TOO LATE!
                """
        }],
    'BE REALISTIC': [-5, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                There's no way out Berthold. What you have done is too serious. 
                The only question is whether you take another life.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                It's not up to you. I'm holding all the cards.
                (Points the gun at Annie)
                IF I DIE, SHE DIES! You hear me?
                """
        }],
    'TALK INSANITY': [-5, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I know you are in distress Berthold. You are not in your right mind. 
                We are going to find you a doctor and everything will be fine.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I DON'T NEED TO BE CURED! I am thinking perfectly. But my eyes are open now.
                I won't let anyone hurt me again. EVER!
                """
        }]
    }


def talk_to_kidnapper():
    # Display the instruction and the emotional choices
    instruction = f"""
                -----
                Earn {kidnapper.name}'s trust. Choose on what you want to say:
                """
    instruction = dedent(instruction)
    emotions_list = [key for key in emotions_dict.keys()]       # Make a list of all playable emotions
    emotions_nums = [i+1 for i in range(len(emotions_list))]    # Get the numbers of playable emotions
    for i in emotions_nums:
        instruction += f"\t {i} - {emotions_list[i-1]}\n"
    print(instruction)

    # Let player choose what to say to the Hostage Taker
    inp_num = ask_int("Enter chosen number: ", emotions_nums)   # Ask player for number of chosen emotion
    inp_str = emotions_list.pop(inp_num-1)                      # Remove the chosen emotion from the list
    print(f"You have chosen {inp_num} - {inp_str.title()}")

    # Execute the chosen emotion script
    script = emotions_dict.pop(inp_str)
    for values in script[1].values():
        print(f"{values}")
        time.sleep(set_time)


