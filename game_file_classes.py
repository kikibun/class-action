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
            elif bakery_visit == True and nosy_counter == 0:
                print "You look at the police station. Your...bag of herbs...weighs heavily in your pocket.\n"
                return 'station_decision'
            elif nosy_counter == 1:
                print "The police station looms large in the distance, but you approach it with conviction!\n"
                return 'police_room'
            else:
                print "A fourth scenario has occured."
                return 'police_room'

        else:
            if bakery_visit == False:
                print "Maybe you should consider the bakery."
                return 'town_square'
            elif bakery_visit == True and nosy_counter == 0:
                print "You look at the bakery, but it doesn't seem likely that she'll want you to come back again so soon."
                return 'town_square'
            elif nosy_counter == 1:
                print "Suddenly, this small town gives you a strange feeling."
                print "Maybe you'll come back another time."
                exit(0)

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

class ButcherFront(Room):
    def enter(self):
        print "You nervously clear your throat."
        print "'Um, the baker sent me? I have an item for you', you say."
        return 'butcher_back'

class ButcherBack(Room):
    def enter(self):
        print "Butcher: 'The baker? So you've seen the garden?'\n"
        action = raw_input("> ")

        if action in ['yea', 'yes', 'yep', 'yeah']:
            print "The butcher laughs."
            print "Butcher: 'Well, at least you admit it. Give me the thing, then.'\n"
            print "You hand the box to the butcher."
            print "Your mission accomplished, you leave the butcher's shop.\n"
            print "You hurry home to try the herbs."
            print "Amazing."
            exit(0)

        elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
            print "Butcher: 'So you must have stolen the box then!'"
            print "Butcher: 'Nobody steals from the baker!'\n"
            print "The butcher pulls her hatchet out of the wood block."
            print "Butcher: 'I think it's time for you to get out. Give me the box and go.'\n"
            print "Shaken, you hand the butcher the box and run out of the shop."
            print "You're lucky to escape with your life.\n"
            print "Maybe next time will go more smoothly."
            exit(0)

        else:
            print "Butcher: 'Why don't we try that one again...'"
            return 'butcher_back'

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
        print "You walk through the doors of the police station."
        print "Looking around, you see a reception desk toward the back of the reception area.\n"

        if nosy_counter == 1:
            print "You approach the reception desk."
            print "'Excuse me', you say, 'is Officer Greene available?'"
            print "The bored-looking secretary glances at you.\n"
            print "Secretary: 'Just a moment. Please have a seat.'"
            print "She gestures at the plastic chairs lining the north wall of the room.\n"
            print "After a brief wait, an Officer comes out from the rear of the station.\n"
            return 'officer_visit'

        else:
            print "There is a secretary at the reception desk. She looks up, and sees you by the door."
            print "Secretary: 'Can I help you with something?'"
            action = raw_input("> ")

            if action in ['yes', 'yea', 'yeah']:
                print "Secretary: 'What is it? Do you have a crime to report?'"
                action = raw_input("> ")
                if action in ['yea', 'yes', 'yeah']:
                    print "Secretary: 'Officer Harrigan, can you come over here please? This person would like to report a crime.'"
                    print "You give your statement to the officer, selling out the baker as a purveyor of unique herbs."
                    print "What a buzz-kill.\n"
                    print "You slink out of the town, people shaking their heads as you pass."
                    print "For shame."
                    exit(0)

                elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
                    print "Secretary: 'Are you sure? You look a little shifty.'"
                    print "She waves to an officer nearby."
                    print "Secretary: 'Officer Harrigan, will you check this person out? Something is off with them.'\n"
                    print "The officer searches you and finds your herbs.\nShe shakes her head sadly."
                    print "Officer: 'I'm going to have to confiscate these herbs, they could be dangerous in the wrong hands!'\n"
                    print "She shoos you out the door.\nYou walk dejectedly out of the police station."
                    print "Better luck next time."
                    exit(0)

                else:
                    print "Secretary: 'If you're going to waste time, do it somewhere else.'"
                    print "The secretary points to the door.\nYou take the hint, and leave."
                    print "You decide to quit while you're ahead, and head home with your herbs.\n"
                    print "Awesome."
                    exit(0)

            elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
                print "Secretary: 'This is a police station, not a museum. Gawk somewhere else.'"
                print "The secretary returns to her paperwork, dismissing you."
                print "You've had enough of the law for one day.\nTime to head home!\n"
                print "Righteous."
                exit(0)

            else:
                print "Secretary: 'I can't stand a mumbler! Come back when you've learned to speak clearly.'"
                print "The secretary glares at you."
                print "Startled, you back out of the police station.\n"
                print "At least you have your herbs to comfort you."
                print "Tubular."
                exit(0)

class Officer(Room):
    def enter(self):
        print "Officer: 'Are you the idiot asking for Officer Greene?'"
        print "You nod. She looks mad.\n"
        print "Officer: 'Did the baker send you?'"
        action = raw_input("> ")

        if action in ['yes', 'yea', 'yeah']:
            print "The officer rolls her eyes."
            print "Officer: 'The baker is a valuable part of our economy.'"
            print "Officer: 'Forget you ever met her, and forget your way back here.'\n"
            print "The officer stalks off.\n"
            print "Secretary: 'That means it's time for you to go, honey.'\n"
            print "You get up, shaken, and leave the station."
            print "You just wanted a brownie!"
            exit(0)

        elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
            print "Officer: 'I don't believe for a second that was just a lucky guess.'"
            print "Officer: 'Whatever game you're playing, play it somewhere else.'\n"
            print "The officer glares at you.\nYou stand up and leave the station.\n"
            print "You can't help but feel you dodged a bullet."
            print "What a strange town."
            exit(0)

        else:
            print "Officer: 'Whatever. I don't think you're welcome in our town anymore.'"
            print "Officer: 'Maybe it's time for you to leave.'\n"
            print "You leave the police station, wondering what you just got yourself into."
            print "Oh well, there's a Sbux on the way home."
            exit(0)

class Map(object):
    rooms = {
        'town_square' : TownSquare(),
        'bakery_room' : Bakery(),
        'garden' : Garden(),
        'butcher_room' : ButcherFront(),
        'police_room' : PoliceStation(),
        'station_decision' : Decision(),
        'officer_visit' : Officer(),
        'butcher_back' : ButcherBack()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.rooms.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('town_square')
a_game = GameEngine(a_map)
a_game.play()
