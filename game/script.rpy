# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Detective = Character("Detective")
define whois = Character("???")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with Fade (1.0, 0.5, 1.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    "It was just like any other night in this cold city... the towering skyscrappers obscuring the nightsky..."

    "it's this heavy mood that fills you with dread of the unknown... anyone could jump at this moment and surprise you with your guard lowered..."

    "Hidden in plain sight... expecting the right moment to strike... I knew i shouldn't have taken that path back home."

    whois "Your time is out... it's time for payback"

    "BANG"

    #after this add a flash and then the scene changes to new thing

    scene bg room
    with fade
    
    "...whew what a night those cats couldnt stop screaming"

    show eileen happy
    with fade

    Detective "hell yeah ."



    # This ends the game.

    return
