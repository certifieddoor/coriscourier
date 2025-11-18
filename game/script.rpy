# The game starts here.



# persistent variables
default persistent.secret_unlocked = False
default persistent.parallax_on = True 


# this set of variables is just a bunch of fun stats
define total_rolled = 0 # this is the total for the dice you've ever ever rolled!!!!
define total_rolls = 0 # total amount of times you've rolled individual dice (if your stat is 4, it will add 4)
define total_rtimes = 0 # total amount of times you've done a roll (no matter your stat, it will add 1 each time)
# maybe I will add persistence, or maybe not.


# this set of variables controls the "free", "easy", "medium", "hard", "veryhard", "impossible"
define free = 1
define easy = 6
define avg = 12
define hard = 18
define stp = 24
define imp = 30
define ezd = {"free" : free, "easy" : easy, "avg" : avg, "hard" : hard, "stp" : stp, "imp" : imp }

# this set of variables is the five stats. the stats are around 1-7, but players can choose to surpass the limit of 20 if they wish
# one less than average becauser my sliders are bad. and I want each stat to be at least 1.
define p = 3
define a = 3
define w = 3
define g = 3
define t = 3
# maybe I should use a dictionary?
define statd = { "p" : p, "a" : a, "w" : w, "g" : g, "t" : t }


# these are boolean values for the fundamentals of the game
define default_stats = True # usually will always be true, player can customize though?

# this is a list of special ability things???????????????????????????
# I should add special abilities to the shapeshifting presets.
define specials = []

# specific boosts on certain actions in the PAWGT???? requires more thinking tho
# + too much balancing that I don't want to do

# this is a variable displaying the affection that the burden has for cori. rico? iro?
# uses the same scaling as pawgt. can be negative? (so I don't have to balance too hard)
# no wait it should remain at least 0 so the bar shows...okay
#
define caff = 4 # "cori affection"
# 0 affection: 4 course meal :3
# 1-2 affection: 3 course meal
# 3-5 affection: 2 or 3 course meal
# 6 affection: 1-2 dishes
# 7 affection: 0-1 dishes

# this is a list of lists of the possible dishes that the burden may ask cori to pick up, indexes based on caff
define dishes = [
    [ # 0 affection what did you do....these are kinda impossible good luck
        "meme", "conlang", "architecture", "graffiti"
    ],
    [ # 1 hard to find around (such as needing to infiltrate a museum) or hard to bring to the hungry
        "glass blowing", "industrial design", "sculpture", "body paint"
    ],
    [ # 2.. even more confusing to bring to the hungry? or hard to find around
        "music composition", "pottery", "musical performance", "printmaking"
    ],
    [ # 3 it's okay but how do you "bring it" to the hungry?????
        "theatre", "cinema", "dance", "performance art"
    ],
    [ #4 decently easy to find/make
        "character design", "animation",  "calligraphy", "fashion design"
    ],
    [ # 5 games & fun stuff, pretty popular
        "video game", "visual novel", "board game", "comic book"
    ],
    [ # 6 these are decently easy to find
        "photography", "poetry", "graphic design", "painting"
    ],
    [ # 7 nice jobb. these are easy ish to get
        "literature", "cuisine", "drawing", "anything"
    ]
]
define dishes_cooked = []
# add dishes to dishes_cooked once cooked. 

# have a list of tuples? list.index(string of the thing) + 1
# list in the format of ["art form", [(list of tuples for menu choice and what label it jumps to)]]
# copy pasting dies' code for reference
    # $ randomcount = renpy.random.randint(2,5) // amount of dishes left to get or something
    # $ the_options = renpy.random.sample(lst_c3, randomcount)
    # $ chosen_thing = menu(the_options)
    # $ renpy.jump(chosen_thing)

# OK DISHES
# 32 total: add character design, music composition, ANYTHING, subtley ??? meme ones?? 4 in each
# art: conlang, cuisine, painting, animation, video game, visual novel, comic book, drawing, board game, fashion design
# graphic design is my passion, literature, pottery, theatre, dance, graffiti
# glass blowing, industrial design, music performance,  photography, poetry, performance art, printmaking, sculpture
# architecture, body paint, calligraphy, cinema
# harder ones (like graffiti + architecture + conlangs + etc because....how do you bring that home lol.....) on lower indices (indexes?)



# this is a list: index of number is the adjective describing the thing
define statjudge = ["completely nonexistent", "horribly lacking", "mildly lacking","below average","average","good","pretty great","perfect","more than perfect"]


# this is a collection of transitions

define dizoom = MultipleTransition([
    False, zoomout, True
])

define funswing = Swing(0.5,True,True,background="#c0f533",flatten=False)

transform rotation:
    alignaround (.5, .5)
    rotate 0
    linear 0.5 rotate 360 #5 seconds, 360 degrees
    repeat 1

transform squishysquash:
    anchor (0.5,0.5)
    linear 0.4 yzoom(1.01)
    linear 0.4 yzoom(1.0)
    repeat 
# this is a function to roll things.
# inside this init python is a bunch of functions, classes and stuff.
init python:
    def roll_dice(n):
        # n is the stat of pawgt, returns the total from rolling
        tot = 0
        for i in range(n):
            tot += renpy.random.randint(1,6)
        return tot
    def stat_check(s):
        # s is a string containing one of "pawgt"
        return roll_dice(statd[s])
    def passed_check(s,t):
        # s is a string free, easy, avg, hard, stp or imp
        # t is an int containing what the roll_dice returned
        # this returns a boolean True/False
        # greater than OR equal to will work
        return t >= ezd[s]

# start defining characters here

define c = Character("CORI",color="c0f533")
define y = Character("THE HUNGRY", color="#fd761f")

label start:
    # $ renpy.notify("Hello. this is a notification.")
    # add parallaxes this time :))
    # dissolve for cool things
    # better UI too (need to plan that out)
    # better names

    scene bg fill white
    show cori human test at truecenter, squishysquash
    show screen parallaxparticles1 
    # show screen bars

    # c "helo (help this gui is so scuffed ToT how to design boxes)"
    # c "bagel"
    # c "p is more now"
    # $ p += 1
    # c "lookie!"

    show screen caffection
    # c "ysyy!"
    # $ caff += 2
    # c "yipiiee they like me!"

    show screen choosep
    show screen choosea
    show screen choosew
    show screen chooseg
    show screen chooset

    show screen showp
    show screen showps
    show screen showa
    show screen showas
    show screen showw
    show screen showws
    show screen showg
    show screen showgs
    show screen showt
    show screen showts
    show screen stot

    c "choose your PAWGT by sliding the sliders hooray. click the text box to learn more (this is also buffer for people who accidentally click not the slider)"
    c "PHYS is for strength-related things."
    c "ACTS determine your motivation to persist."
    c "WORDS influence your ability to speak with others."
    c "GIFTS bring you more ideas and observations."
    c "And TIME allows you to do things fast."
    c "the game is balanced for a total of 20, but you can choose to gamble more or less :)"


    hide screen choosep 
    hide screen choosea
    hide screen choosew 
    hide screen chooseg 
    hide screen chooset

    hide screen showp
    hide screen showps 
    hide screen showa
    hide screen showas 
    hide screen showw
    hide screen showws 
    hide screen showg
    hide screen showgs 
    hide screen showt
    hide screen showts 

    hide screen stot

    $ p += 1
    $ a += 1
    $ w += 1
    $ g += 1
    $ t += 1
    $ statd = { "p" : p, "a" : a, "w" : w, "g" : g, "t" : t }

    y "you chose [p] p, [a] a, [w] w, [g] g and [t] t."

    y "{color=#c0f533}CORI{/color}, welcome to Cori's Courier."

    hide screen caffection 
    scene whoahwoaho
    with funswing
    pause 0.2 
    scene curveyone
    with dissolve
    show upsidedown:
        xalign 0.5
        yalign 0.5 
        rotation 
    pause 
    ""


    
    # "let's try our first gamble."
    # "let's see if we can pass this EASY test with our physical stat!"
    # "my physical stat is [statjudge[p]] apparently"
    # if passed_check("easy",stat_check("p")):
    #     "I passed!"
    # else:
    #     "I failed :("


    # This ends the game.
    # 0 affection: 4 course meal :3
    # 1-2 affection: 3 course meal
    # 3-5 affection: 2 or 3 course meal
    # 6 affection: 1-2 dishes
    # 7 affection: 0-1 dishes

    return

label select_stats:
    scene bg fill white

    "another chapter, another stats shift."

    show screen choosep
    show screen choosea
    show screen choosew
    show screen chooseg
    show screen chooset

    show screen showp
    show screen showps
    show screen showa
    show screen showas
    show screen showw
    show screen showws
    show screen showg
    show screen showgs
    show screen showt
    show screen showts
    show screen stot

    "Again, the game is balanced for a total of 20, but you can choose to gamble more or less :)"

    hide screen choosep 
    hide screen choosea
    hide screen choosew 
    hide screen chooseg 
    hide screen chooset

    hide screen showp
    hide screen showps 
    hide screen showa
    hide screen showas 
    hide screen showw
    hide screen showws 
    hide screen showg
    hide screen showgs 
    hide screen showt
    hide screen showts 

    hide screen stot

    $ p += 1
    $ a += 1
    $ w += 1
    $ g += 1
    $ t += 1
    $ statd = { "p" : p, "a" : a, "w" : w, "g" : g, "t" : t }

    y "you chose [p] p, [a] a, [w] w, [g] g and [t] t."

label chapter_3:
    # feed the burden
    y "too much chitchat! I am hungry."

label aff_0:
    y "you know..... I think I'm REALLY craving a 4 course meal today :3"
    y "yes, FOUR pieces of art :D"
    y "you can do it, I believe in you :)"

label aff_12:
    y "I think I'd like a CLASSIC 3 course meal today! :3"
    y "three pieces of art AS SOON AS POSSIBLE!"
    Y "better get to work :)"

label aff_35:
    $ fatesealer = renpy.random.randint(2,3)
    if fatesealer == 2:
        y "hmmm! after a bit of thinking, I've decided I'm going to be nice."
        y "get me TWO DELICIOUS DISHES!"
    else:
        y "hmmm! after a bit of thinking, I've decided I'm going to be...less nice"
        y "get me THREE delicious dishes AS SOON AS POSSIBLE!"

label aff_6:
    $ fatesealer = renpy.random.randint(1,2)
    if fatesealer == 2:
        y "HMM! You've been so nice to me, but I feel like being just a bit needy :3"
        y "get me TWO DELICIOUS DISHES!"
    else:
        y "I'm letting my stomach make it easy for you!"
        y "get me ONE DELICIOUS DISH!"

label aff_7:
    $ fatesealer = renpy.random.randint(0,1)
    if fatesealer == 1:
        y "I'm letting my stomach make it easy for you!"
        y "get me ONE DELICIOUS DISH!"
    else:
        y "My stomach is SUPER KIND today!"
        y "It is not very hungry :) I won't demand a dish this time!"
        y "don't forget to thank me by continuing to be nice :3"

