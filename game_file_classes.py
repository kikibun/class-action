# bakery adventure but with classes instead of functions
import random
nosy_counter = 0
police_officer = False
bakery_visit = False

class Room(object):
    def enter(self):
#        #this is where room text goes
        pass

class GameEngine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('exit')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            print next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class TownSquare(Room):
    def enter(self):
        global bakery_visit
        print "You are in the center of a small town.\n Ahead, you see a bakery, a butcher, and a police station."
        print "You decide to look around.\n Which do you enter?"
        action = raw_input("> ")

        if action == "bakery":
            if bakery_visit == False:
                print "You approach the bakery. It is evident the baker has been busy!\n"
                return 'bakery_room'
            else:
                print "You look back at the bakery. There's no going back now...\n"
                return 'town_square'

        elif action == "butcher":
            if bakery_visit == False:
                print "You start to approach the butcher, but she looks kind of mean. \n Maybe you will come back later.\n"
                return 'town_square'
            else:
                print "You enter the butchery. The bell over the shop door chimes, and the butcher looks up from the counter."
                print "You notice she has a very large meat cleaver.\n"
                return 'butcher_room'

        elif action == "police station":
            if bakery_visit == False:
                print "For a sleepy little town, there sure is a large police station. \n You wonder how many officers are staffed."
                print "Thinking about that makes you hungry. You always get hungry when you're nervous.\n"
                return 'town_square'
            else:
                print "You look at the police station. Your...bag of herbs...weighs heavily in your pocket.\n"
                return 'station_decision'

class Bakery(Room):
    def enter(self):
        global nosy_counter, police_officer
        if nosy_counter == 1:
            print "That baker seemed a little paranoid. Maybe you should wait a while before you bug her again."
            return 'town_square'

        print "You walk into a bakery and see many snacks. Do you choose sweet or savory?"
        snack = raw_input("> ")

        if snack == "sweet":
            print "Baker: 'Ah, a sweet tooth!'\nDo you choose chocolate cake, carrot cake, or red velvet cake?"

            cake = raw_input("> ")

            if cake == "chocolate cake" or cake == "chocolate":
                print "Baker: 'Oh, we're actually sold out of that, sorry.'"
                if police_officer == True:
                    print "Baker: 'But let me give you this instead to thank you for your service.'\nYou reveive a glazed donut."
                    exit(0)
                else:
                    print "'Come back tommorow and try again!' \nYou exit the bakery."
                    exit(0)
            elif cake == "carrot cake" or cake == "carrot":
                print "Baker: 'Excellent choice.'"
                if police_officer == True:
                    print "To your surprise, the baker has drawn your badge in the icing. Nice!"
                    exit(0)
                else:
                    print "You take your cake and leave. Bye!"
                    exit(0)
            elif cake == "red velvet cake" or cake == "red velvet":
                if police_officer == True:
                    print "Baker: 'Uh....why don't you take this instead.'\n You received a glazed donut."
                    exit(0)
                else:
                    print "The cake was poisoned. You die in agony. Sorry."
                    exit(0)
            else:
                print "Baker: 'Sorry, we don't have that. Maybe we'll have %s tomorrow!'" % cake
                exit(0)

        elif snack == "savory":
            print "Baker: 'I see, something with less sugar in it. Would you like a meat pie? Quiche? Something...else?'"

            savory = raw_input("> ")

            if savory == "meat pie":
                print "Baker: 'Ham, beef, or long pig?'"

                meat_pie = raw_input("> ")

                if meat_pie == "ham":
                    if police_officer == True:
                        print "The baker smirks about the irony, but hands you the pie regardless."
                        exit(0)
                    else:
                        print "You receive a meat pie. Congrat."
                        exit(0)
                elif meat_pie == "beef":
                    if police_officer == True:
                        print "The baker slips a little something in the bag. It's another meat pie! Aw."
                        exit(0)
                    else:
                        print "You receive a meat pie. It's okay."
                        exit(0)
                elif meat_pie == "long pig":
                    if police_officer == True:
                        print "Baker: 'You know what...why don't you take this instead.'\nYou receive a glazed donut."
                        exit(0)
                    else:
                        print "Baker: 'Are you sure? Well...alright then.'"
                        print "You receive your meat pie. It's a little gamey."
                        exit(0)
                else:
                    print "You get nothing. The baker is a busy woman, don't waste her time."
                    exit(0)

            elif savory == "quiche":
                if police_officer == True:
                    print "Baker: 'We've got an armed forces special in the back, let me go grab it.'\nYou receive a slice of tomato bacon quiche."
                    exit(0)
                else:
                    print "Baker: 'Today's quiche is spinach and cheese. Hope you're okay with that.'\nYou receive a slice of quiche."
                    exit(0)

            elif savory in ["What else?", "what else", "what else?"]:
                print "Baker: 'Oh...uh....nothing. Did you still want something sweet or savory?'"
                nosy_counter += 1
                if nosy_counter == 2:
                    print "Baker: 'You ask too many questions. Come back when you know what you want.'\nThe baker glares at you until you leave."
                    exit(0)
                return 'bakery_room'

            elif savory == "something else":
                if police_officer == True and nosy_counter < 1:
                    nosy_counter += 1
                    print "Baker: 'Sorry officer, we don't have any specials today. \nCould I offer you something sweet, or something savory?'\nThe baker sweats nervously."
                elif police_officer == True and nosy_counter == 1:
                    print "Baker: 'You know, I really should get to my other customers. Come back any time.'\nYou take the hint, and leave."
                    exit(0)
                elif police_officer == False:
                    print "Baker: 'Oh...something else you say? Let me see what we have to offer.'"
                    print "Baker: 'We do have some...special items in stock today, but first I gotta ask. You're not the fuzz, are you?'"

                fuzz = raw_input("> ")
                if fuzz in ["yea", "yes", "yeah"]:
                    police_officer = True
                    print "Baker: 'Oh, hello officer! Has anybody offered you the police discount? Something sweet or savory today?'"
                    return 'bakery_room'
                elif fuzz in ["no", "naw", "no way", 'nope']:
                    print "Baker: 'Sorry, I had to ask. You understand.\nPlease follow me into the garden.'"
                    print "You walk around the back of the sales counter, and through a small door."
                    print "You find yourself behind the bakery, where there is a small, but lush, garden!"
                    print "Weird.\n"
                    return 'garden'
                else:
                    print "Baker: 'Hm. I'm not taking any chances. Come back if you want a pie.'\nYou are escorted out of the bakery."
                    exit(0)
            else:
                print "Baker: 'If you aren't going to choose something, you should leave.'"
                exit(0)

        else:
            print "Baker: 'Sorry, we don't have %s today.'\nYou leave the bakery, disappointment evident on your face." % snack
            exit(0)

        print "There are many snacks on display. Do you choose sweet or savory?"

class Garden(Room):
    def enter(self):
        global bakery_visit, nosy_counter
        print "'Wow, there sure is a lot of greenery here', you say.\n'What all do you grow?'"
        print "The baker looks suspciously at you."
        print "Baker: 'That sure is a leading question; you don't have a particular reason for asking, do you?'\n"
        action = raw_input("> ")

        if action in ["no", "nope", "naw", "nah", "no way", "no reason"]:
            print "Baker: 'Well, alright. Can't be too careful.'"
            print "The baker walks toward the back of the garden.\nYou follow her, admiring the plants.\n"
            print "Baker: 'Okay, here we are!'\nShe reaches into a wooden box and pulls out a bag of...dried herbs."
            print "She hands you the baggie."
            print "Baker: 'Here you are. The items as requested.\nBut before you go...I need you to do me a favor.'"
            print "You think this over.\n"
            print "'Alright', you say, 'What is it?'"
            print "Baker: 'I need you to take this to the butcher down the way.' She hands you a small box."
            print "You sigh to yourself."
            print "'I guess I can do that!'\n"
            bakery_visit = True
            return 'town_square'

        elif action in ["yes", "yea", "yeah", "yah", "i do", "I do"]:
            print "Baker: 'You know what, before I give you the Item, I need you to do me a favor."
            print "I need you to go by the police station and tell Officer Greene I've got rats again."
            print "Will that be a problem?'\n"
            print "You nod. That seems easy enough, but suddenly you're starting to get a weird feeling."
            nosy_counter += 1
            bakery_visit = True
            return 'town_square'

        else:
            print "Baker: 'Sorry, I've just remembered I've got some buns in the oven. We need to do this later.'"
            print "She turns around and shoos you back into the shop."
            nosy_counter += 1
            return 'bakery_room'

class Butcher(Room):
    def enter(self):
        print "NO TEXT YET"

class Decision(Room):
    def enter(self):
        print "You consider going in, not going in, or flipping a coin.\nWhat do you decide?"
        action = raw_input("> ")

        if action == 'go in':
            print "You walk towards the police station door.\nWhat could go wrong?\n"
            return 'police_room'

        elif action == 'don\'t go in':
            print "Better to not go in while you've got those herbs.\nSmart.\n"
            return 'town_square'

        elif action == 'flip a coin':
            coin_toss = random.randint(0,1)
            if coin_toss == 1:
                print "The fates have decided: time to face the police station.\n"
                return 'police_room'
            elif coin_toss == 0:
                print "The fates have spoken: you back away from the police station.\n"
                return 'town_square'

        else:
            print "You clearly need to think about this some more.\n"
            return 'town_square'

class PoliceStation(Room):
    def enter(self):
        print "NO TEXT YET"
        action = raw_input("> ")

        if action == "Officer Greene":
            pass

        elif nosy_counter == 1:
            pass

class Map(object):
    rooms = {
        'town_square' : TownSquare(),
        'bakery_room' : Bakery(),
        'garden' : Garden(),
        'butcher_room' : Butcher(),
        'police_room' : PoliceStation(),
        'station_decision' : Decision()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.rooms.get(scene_name)
        print scene_name
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('town_square')
a_game = GameEngine(a_map)
a_game.play()
