# ---------------------------------------- THE IMPORT ---------------------------------------- #

# MODULES
from textwrap import dedent
import characters
import game

# CHARACTERS
player = characters.player
victim = characters.victim
kidnapper = characters.kidnapper
police = characters.police


# ---------------------------------------- ACT SCRIPT ---------------------------------------- #
# EMOTION SCRIPT
emotion_sequence_dict = {
    'BE REALISTIC': [-8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Berthold, what you have done is too serious. There's no way out of this. 
                The only question is whether you take another life.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                It's not up to you. I'm holding all the cards.
                (Points the gun at Annie)
                IF I DIE, SHE DIES! You hear me?"""
        }],
    'CALM HIM DOWN': [8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I need you to calm down, Berthold. Let me help you and everything will be okay.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I don't need your help. Nobody can help me now. JUST LEAVE ME ALONE AND I'LL END THIS."""
        }],
    'MAKE DEMANDS': [0, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I need you to let her go Berthold. That is the only way this can end.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I am not stupid! I know you are going to shoot me the moment I release her.
                This is how this ends. EITHER I DIE, OR WE BOTH DIE!"""
        }],
    'REASSURE HIM': [8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I'm not going to hurt you Berthold. I just want to talk and find a solution.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                Talk!? I don't want to talk. It's too late for that now. IT'S TOO LATE!"""
        }],
    'TALK INSANITY': [-8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I know you are in distress Berthold. You are not in your right mind. 
                We are going to find you a doctor and everything will be fine.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I DON'T NEED TO BE CURED! I am thinking perfectly. But my eyes are open now.
                I won't let anyone hurt me again. EVER!"""
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
                (to Annie): Nobody is going to die. Stay calm. Everything is going to be fine."""
        }]

    }

# ARE YOU ARMED SCRIPT
disarm_sequence_dict = {
    'LIE AND KEEP YOUR GUN': [-8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                No. I don't have a weapon.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                YOU'RE LYING! I know you have a gun.
                """,
        'YOU_2': """        🤵 NEGOTIATOR (YOU)
                I'm telling you the truth Berthold. I came here unarmed."""
        }],
    'ADMIT AND DROP YOUR GUN': [8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Yes. I have a gun right now.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                DROP IT! No sudden moves or I'll shoot you.
                """,
        'YOU_2': """        🤵 NEGOTIATOR (YOU)
                (Drops the gun)
                There. I don't have a gun anymore."""
        }]
    }

# KNOW THE CAUSE SCRIPT
cause_sequence_dict = {
    'ASK FOR THE CAUSE': [0, {
        'YOU_1': f"""        🤵 NEGOTIATOR (YOU)
                I know {victim.name} is your girlfriend Berthold. Why are you doing this to her?
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I love her. You know? More than anything in this world.  We've been together for 
                two years. And I did everything for her. """,
        'BER_2': """
                BUT SHE HAS NEVER LOVED ME BACK. SHE HAD GIVEN ME NOTHING BUT PAIN AND FALSE HOPES. 
                But tonight, it is about to change.
                """,
        'ANN_1': """        👩‍💼 ANNIE
                (afraid and crying)
                (to Berthold): Berthold, please! I'm sorry! I know I made a mistake. 
                 But please, I promise, I won't hurt you ever again.
                """,
        'BER_3': """        🙍‍♂️ BERTHOLD
                (to Annie): Don't worry Annie. I'll make sure you would NEVER hurt me again."""
        }],
    'ASK ABOUT THE DEAD MAN': [0, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                We found a dead man in your room. You shot him, didn't you? What does he have to do 
                with all this?
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                That son of a b**** is my girlfriend's latest affair. Throughout our relationship, 
                I have caught her cheating several times.""",
        'BER_2': """
                But I have always been so forgiving to her. I was hoping that she will change
                eventually. BUT SHE DIDN'T. SHE ONLY TOOK ADVANTAGE OF MY KINDNESS...
                """,
        'ANN_1': """        👩‍💼 ANNIE
                (afraid and crying)
                (to Berthold): Berthold, please! Just let me go. We can start over again. 
                Just give me a chance.
                """,
        'BER_3': """        🙍‍♂️ BERTHOLD
                (to Annie): I've had enough of your excuses and promises, Annie. I am tired of all  
                the pain. You could never fool me again. NEVER!"""
        }]
    }

# LAST EMOTION SCRIPT
last_emotion_sequence_dict = {
    'ASK HIM TO END THIS': [0, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Violence is not the answer Berthold. It is not too late. You can still end this.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                It is too late for that now. Death is the only way for this to stop."""
        }],
    'SYMPATHIZE WITH HIM': [8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Listen Berthold. I know it is not your fault. You're just doing this because 
                of you are in pain and angry.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                No, it is not my fault. I never wanted this. I wanted to have a life with her.
                BUT I WAS NOTHING TO HER!"""
        }],
    'TELL HIS MISTAKE': [-8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Do you think this will solve your problem? Look at what you did Berthold. 
                You have killed a lot of people. Even civilians.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I did not mean to hurt them. This is only about me and her. This is her fault."""
        }]
    }

# FINAL NEGOTIATION SCRIPT
final_negotiation_sequence_dict = {
    'ASK FOR TRUST': [8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                You have to trust me Berthold. Let the hostage go and everything will be fine
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I want everyone to leave...""",
        'BER_2': """\
                And I want a car. When I'm far enough, I'll let her go."""
        }],
    'DECLARE THREAT': [-8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                Listen. There are snipers on every roof. Let the hostage go. You have no other choice.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I want everyone to leave...""",
        'BER_2': """\
                And I want a car. When I'm far enough, I'll let her go."""
        }],
    'GIVE LAST CHANCE': [0, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                I'm your last chance Berthold. If you let it slip, they'll kill you.
                Let the hostage go. You have no other choice.
                """,
        'BER_1': """        🙍‍♂️ BERTHOLD
                I want everyone to leave...""",
        'BER_2': """\
                And I want a car. When I'm far enough, I'll let her go."""
        }]

    }

# COMPROMISE OR REFUSE SCRIPT
compromise_sequence_dict = {
    'COMPROMISE': [+8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                That is impossible Berthold. Let Annie go and I promise, you won't be hurt."""
        }],
    'REFUSE': [-8, {
        'YOU_1': """        🤵 NEGOTIATOR (YOU)
                That is out of the question. Just put the gun down and let Annie go."""
        }]
    }


# ---------------------------------------- GAME PROPER ---------------------------------------- #
# PRE-GAME SEQUENCE
game.print_title()
player.enter_profile()

game.print_overview()
game.talk_with_police()
game.print_mission()

# NEGOTIATION SEQUENCES
game.initial_encounter()

# Emotion-1 sequence
instruction = f"-----\nEarn {kidnapper.name}'s trust. Choose on what you want to say:"
game.talk_to_kidnapper(instruction, emotion_sequence_dict)
game.talk_to_kidnapper(instruction, emotion_sequence_dict)

# Are you armed sequence
instruction = f"-----\n{kidnapper.name} asks you if you are armed."
instruction += """
        🙍‍♂️ BERTHOLD
                (points the gun at you)
                Are you armed?
                """
game.talk_to_kidnapper(instruction, disarm_sequence_dict, True)

# Emotion-2 sequence
instruction = f"-----\nEarn {kidnapper.name}'s trust. Choose on what you want to say:"
game.talk_to_kidnapper(instruction, emotion_sequence_dict)
game.talk_to_kidnapper(instruction, emotion_sequence_dict)

# Know the cause sequence
instruction = f"-----\nUnderstand {kidnapper.name}'s reason for doing the hostage."
game.talk_to_kidnapper(instruction, cause_sequence_dict)
game.talk_to_kidnapper(instruction, cause_sequence_dict)

# Last emotion sequence
instruction = f"-----\nEarn {kidnapper.name}'s trust. Choose on what you want to say:"
game.talk_to_kidnapper(instruction, last_emotion_sequence_dict)

# Final Negotiation Sequence
instruction = f"-----\nAppeal to {kidnapper.name} for the last time."
game.talk_to_kidnapper(instruction, final_negotiation_sequence_dict)

# Compromise or refuse sequence
instruction = f"Compromise or refuse on {kidnapper.name}'s demand?"
game.talk_to_kidnapper(instruction, compromise_sequence_dict)

# Finale Sequence
game.final_decision()

# Game Completion
game.print_completion()
