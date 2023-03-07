# IMPORT MODULE
from textwrap import dedent
import time
import characters

# CHARACTERS
player = characters.player


# FUNCTIONS
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
        
        >>> enter to continue
        """
    input(f"{dedent(text)}")


def print_overview():
    text = """\
        -----
        One late evening, you arrive at an office at the top floor of a high rise residential building.
        The police approached you.\
        """
    input(f"{dedent(text)}")


def talk_with_police():
    pol_1 = """\
    POLICE OFFICER
        \""" Good evening sir! We have a hostage situation happening at the outdoor lounge at the rooftop of
        this building. A man is holding his girlfriend at gunpoint. We already have the snipers in position.
        However, we can't risk shooting the man. If we miss, the girl can get shot.
        \"""    
    """
    you_1 = """\
    NEGOTIATOR (YOU)
        \""" Do you know his motives?
        \"""    
    """
    pol_2 = """\
    POLICE OFFICER
        \""" We have no clue sir. But we did find a dead man in their room. Apparently, he was shot.
        We suspect this has something to do about their relationship.
        \"""    
    """
    you_2 = """\
    NEGOTIATOR (YOU)
        \""" Any other casualties?
        \"""    
    """
    pol_3 = """\
    POLICE OFFICER
        \""" Well sir, he has also already killed two of our responding policemen. He also killed two
        civilians and wounded one. That wounded one is currently outside where the hostage is happening.
        It's a teenage boy. He needs urgent medical attention, but it is too dangerous to approach.
        \"""    
    """
    you_3 = """\
    NEGOTIATOR (YOU)
        \""" That's unfortunate. It seems the man is really twisted right now.
        \"""    
    """
    pol_4 = """\
    POLICE OFFICER
        \""" I agree sir. But we still need to save the girl at all cost.
        \"""    
    """
    you_4 = """\
    NEGOTIATOR (YOU)
        \""" I know. Do you have their names?
        \"""    
    """
    pol_5 = """\
    POLICE OFFICER
        \""" Yes sir, the man's name is Berthold, and the girl's is Annie.
        \"""    
    """
    you_5 = """\
    NEGOTIATOR (YOU)
        \""" That is all I need. Thank you.
        \"""    
    """

    text_list = [pol_1, you_1, pol_2, you_2, pol_3, you_3, pol_4, you_4, pol_5, you_5]

    for text in text_list:
        print(f"{text}")
        time.sleep(.05)
    input(">>> enter to continue")


def print_mission():
    text = f"""
        --------------------------------------------------------------------------------------------
        MISSION: Talk with Berthold and gain his trust. 
                 Save the girl at all cost.
        --------------------------------------------------------------------------------------------
        
        >>> enter to continue
        """
    input(f"{dedent(text)}")


