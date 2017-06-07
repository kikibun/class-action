import time
import random

nosy_counter = 0
police_officer = False
bakery_visit = False

class Room(object):
    def enter(self):
#        #this is where room text goes
        pass
def print_slow(text):
    time.sleep(1.5)
    print(text)

class TownSquare(Room):
    def enter(self):
        global bakery_visit
        print_slow("You are in the center of a small town.\nAhead, you see a bakery, a butcher, and a police station.")
        print_slow("You decide to look around.\nWhich do you enter?")
        action = raw_input("> ")

        if action == "bakery":
            if bakery_visit == False:
                print_slow("You approach the bakery. It is evident the baker has been busy!\n")
                return 'bakery_room'
            else:
                print_slow("You look back at the bakery. There's no going back now...\n")
                return 'town_square'

        elif action == "butcher":
            if bakery_visit == False:
                print_slow("You start to approach the butcher, but she looks kind of mean. \n Maybe you will come back later.\n")
                return 'town_square'
            else:
                print_slow("You enter the butchery. The bell over the shop door chimes, and the butcher looks up from the counter.")
                print_slow("You notice she has a very large meat cleaver.\n")
                return 'butcher_room'

        elif action == "police station":
            if bakery_visit == False:
                print_slow("For a sleepy little town, there sure is a large police station. \n You wonder how many officers are staffed.")
                print_slow("Thinking about that makes you hungry. You always get hungry when you're nervous.\n")
                return 'town_square'
            elif bakery_visit == True and nosy_counter == 0:
                print_slow("You look at the police station. Your...bag of herbs...weighs heavily in your pocket.\n")
                return 'station_decision'
            elif nosy_counter == 1:
                print_slow("The police station looms large in the distance, but you approach it with conviction!\n")
                return 'police_room'
            else:
                print_slow("A fourth scenario has occurred.")
                return 'police_room'

        else:
            if bakery_visit == False:
                print_slow("Maybe you should consider the bakery.")
                return 'town_square'
            elif bakery_visit == True and nosy_counter == 0:
                print_slow("You look at the bakery, but it doesn't seem likely that she'll want you to come back again so soon.")
                return 'town_square'
            elif nosy_counter == 1:
                print_slow("Suddenly, this small town gives you a strange feeling.")
                print_slow("Maybe you'll come back another time.")
                exit(0)


class Bakery(Room):
    def enter(self):
        global nosy_counter, police_officer
        if nosy_counter == 1:
            print_slow("That baker seemed a little paranoid. Maybe you should wait a while before you bug her again.")
            return 'town_square'

        print_slow("You walk into a bakery and see many snacks. Do you choose sweet or savory?")
        snack = raw_input("> ")

        if snack == "sweet":
            print_slow("Baker: 'Ah, a sweet tooth!'\nDo you choose chocolate cake, carrot cake, or red velvet cake?")

            cake = raw_input("> ")

            if cake == "chocolate cake" or cake == "chocolate":
                print_slow("Baker: 'Oh, we're actually sold out of that, sorry.'")
                if police_officer == True:
                    print_slow("Baker: 'But let me give you this instead to thank you for your service.'\nYou reveive a glazed donut.")
                    exit(0)
                else:
                    print_slow("'Come back tommorow and try again!' \nYou exit the bakery.")
                    exit(0)
            elif cake == "carrot cake" or cake == "carrot":
                print_slow("Baker: 'Excellent choice.'")
                if police_officer == True:
                    print_slow("To your surprise, the baker has drawn your badge in the icing. Nice!")
                    exit(0)
                else:
                    print_slow("You take your cake and leave. Bye!")
                    exit(0)
            elif cake == "red velvet cake" or cake == "red velvet":
                if police_officer == True:
                    print_slow("Baker: 'Uh....why don't you take this instead.'\n You received a glazed donut.")
                    exit(0)
                else:
                    print_slow("The cake was poisoned. You die in agony. Sorry.")
                    exit(0)
            else:
                print_slow("Baker: 'Sorry, we don't have that. Maybe we'll have %s tomorrow!'" % cake)
                exit(0)

        elif snack == "savory":
            print_slow("Baker: 'I see, something with less sugar in it. Would you like a meat pie? Quiche? Something...else?'")

            savory = raw_input("> ")

            if savory == "meat pie":
                print_slow("Baker: 'Ham, beef, or long pig?'")

                meat_pie = raw_input("> ")

                if meat_pie == "ham":
                    if police_officer == True:
                        print_slow("The baker smirks about the irony, but hands you the pie regardless.")
                        exit(0)
                    else:
                        print_slow("You receive a meat pie. Congrat.")
                        exit(0)
                elif meat_pie == "beef":
                    if police_officer == True:
                        print_slow("The baker slips a little something in the bag. It's another meat pie! Aw.")
                        exit(0)
                    else:
                        print_slow("You receive a meat pie. It's okay.")
                        exit(0)
                elif meat_pie == "long pig":
                    if police_officer == True:
                        print_slow("Baker: 'You know what...why don't you take this instead.'\nYou receive a glazed donut.")
                        exit(0)
                    else:
                        print_slow("Baker: 'Are you sure? Well...alright then.'")
                        print_slow("You receive your meat pie. It's a little gamey.")
                        exit(0)
                else:
                    print_slow("You get nothing. The baker is a busy woman, don't waste her time.")
                    exit(0)

            elif savory == "quiche":
                if police_officer == True:
                    print_slow("Baker: 'We've got an armed forces special in the back, let me go grab it.'\nYou receive a slice of tomato bacon quiche.")
                    exit(0)
                else:
                    print_slow("Baker: 'Today's quiche is spinach and cheese. Hope you're okay with that.'\nYou receive a slice of quiche.")
                    exit(0)

            elif savory in ["What else?", "what else", "what else?"]:
                print_slow("Baker: 'Oh...uh....nothing. Did you still want something sweet or savory?'")
                nosy_counter += 1
                if nosy_counter == 2:
                    print_slow("Baker: 'You ask too many questions. Come back when you know what you want.'\nThe baker glares at you until you leave.")
                    exit(0)
                return 'bakery_room'

            elif savory == "something else":
                if police_officer == True and nosy_counter < 1:
                    nosy_counter += 1
                    print_slow("Baker: 'Sorry officer, we don't have any specials today. \nCould I offer you something sweet, or something savory?'\nThe baker sweats nervously.")
                elif police_officer == True and nosy_counter == 1:
                    print_slow("Baker: 'You know, I really should get to my other customers. Come back any time.'\nYou take the hint, and leave.")
                    exit(0)
                elif police_officer == False:
                    print_slow("Baker: 'Oh...something else you say? Let me see what we have to offer.'")
                    print_slow("Baker: 'We do have some...special items in stock today, but first I gotta ask. You're not the fuzz, are you?'")

                fuzz = raw_input("> ")
                if fuzz in ["yea", "yes", "yeah"]:
                    police_officer = True
                    print_slow("Baker: 'Oh, hello officer! Has anybody offered you the police discount? Something sweet or savory today?'")
                    return 'bakery_room'
                elif fuzz in ["no", "naw", "no way", 'nope']:
                    print_slow("Baker: 'Sorry, I had to ask. You understand.\nPlease follow me into the garden.'")
                    print_slow("You walk around the back of the sales counter, and through a small door.")
                    print_slow("You find yourself behind the bakery, where there is a small, but lush, garden!")
                    print_slow("Weird.\n")
                    return 'garden'
                else:
                    print_slow("Baker: 'Hm. I'm not taking any chances. Come back if you want a pie.'\nYou are escorted out of the bakery.")
                    exit(0)
            else:
                print_slow("Baker: 'If you aren't going to choose something, you should leave.'")
                exit(0)

        else:
            print_slow("Baker: 'Sorry, we don't have %s today.'\nYou leave the bakery, disappointment evident on your face." % snack)
            exit(0)

        print_slow("There are many snacks on display. Do you choose sweet or savory?")

class Garden(Room):
    def enter(self):
        global bakery_visit, nosy_counter
        print_slow("'Wow, there sure is a lot of greenery here', you say.\n'What all do you grow?'")
        print_slow("The baker looks suspciously at you.")
        print_slow("Baker: 'That sure is a leading question; you don't have a particular reason for asking, do you?'\n")
        action = raw_input("> ")

        if action in ["no", "nope", "naw", "nah", "no way", "no reason"]:
            print_slow("Baker: 'Well, alright. Can't be too careful.'")
            print_slow("The baker walks toward the back of the garden.\nYou follow her, admiring the plants.\n")
            print_slow("Baker: 'Okay, here we are!'\nShe reaches into a wooden box and pulls out a bag of...dried herbs.")
            print_slow("She hands you the baggie.")
            print_slow("Baker: 'Here you are. The items as requested.\nBut before you go...I need you to do me a favor.'")
            print_slow("You think this over.\n")
            print_slow("'Alright', you say, 'What is it?'")
            print_slow("Baker: 'I need you to take this to the butcher down the way.' She hands you a small box.")
            print_slow("You sigh to yourself.")
            print_slow("'I guess I can do that!'\n")
            bakery_visit = True
            return 'town_square'

        elif action in ["yes", "yea", "yeah", "yah", "i do", "I do"]:
            print_slow("Baker: 'You know what, before I give you the Item, I need you to do me a favor.")
            print_slow("I need you to go by the police station and tell Officer Greene I've got rats again.")
            print_slow("Will that be a problem?'\n")
            print_slow("You nod. That seems easy enough, but suddenly you're starting to get a weird feeling.")
            nosy_counter += 1
            bakery_visit = True
            return 'town_square'

        else:
            print_slow("Baker: 'Sorry, I've just remembered I've got some buns in the oven. We need to do this later.'")
            print_slow("She turns around and shoos you back into the shop.")
            nosy_counter += 1
            return 'bakery_room'

class ButcherFront(Room):
    def enter(self):
        print_slow("You nervously clear your throat.")
        print_slow("'Um, the baker sent me? I have an item for you', you say.")
        return 'butcher_back'

class ButcherBack(Room):
    def enter(self):
        print_slow("Butcher: 'The baker? So you've seen the garden?'\n")
        action = raw_input("> ")

        if action in ['yea', 'yes', 'yep', 'yeah']:
            print_slow("The butcher laughs.")
            print_slow("Butcher: 'Well, at least you admit it. Give me the thing, then.'\n")
            print_slow("You hand the box to the butcher.")
            print_slow("Your mission accomplished, you leave the butcher's shop.\n")
            print_slow("You hurry home to try the herbs.")
            print_slow("Amazing.")
            exit(0)

        elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
            print_slow("Butcher: 'So you must have stolen the box then!'")
            print_slow("Butcher: 'Nobody steals from the baker!'\n")
            print_slow("The butcher pulls her hatchet out of the wood block.")
            print_slow("Butcher: 'I think it's time for you to get out. Give me the box and go.'\n")
            print_slow("Shaken, you hand the butcher the box and run out of the shop.")
            print_slow("You're lucky to escape with your life.\n")
            print_slow("Maybe next time will go more smoothly.")
            exit(0)

        else:
            print_slow("Butcher: 'Why don't we try that one again...'")
            return 'butcher_back'

class Decision(Room):
    def enter(self):
        print_slow("You consider going in, not going in, or flipping a coin.\nWhat do you decide?")
        action = raw_input("> ")

        if action == 'go in':
            print_slow("You walk towards the police station door.\nWhat could go wrong?\n")
            return 'police_room'

        elif action == 'don\'t go in':
            print_slow("Better to not go in while you've got those herbs.\nSmart.\n")
            return 'town_square'

        elif action == 'flip a coin':
            coin_toss = random.randint(0,1)
            if coin_toss == 1:
                print_slow("The fates have decided: time to face the police station.\n")
                return 'police_room'
            elif coin_toss == 0:
                print_slow("The fates have spoken: you back away from the police station.\n")
                return 'town_square'

        else:
            print_slow("You clearly need to think about this some more.\n")
            return 'town_square'

class PoliceStation(Room):
    def enter(self):
        print_slow("You walk through the doors of the police station.")
        print_slow("Looking around, you see a reception desk toward the back of the reception area.\n")

        if nosy_counter == 1:
            print_slow("You approach the reception desk.")
            print_slow("'Excuse me', you say, 'is Officer Greene available?'")
            print_slow("The bored-looking secretary glances at you.\n")
            print_slow("Secretary: 'Just a moment. Please have a seat.'")
            print_slow("She gestures at the plastic chairs lining the north wall of the room.\n")
            print_slow("After a brief wait, an Officer comes out from the rear of the station.\n")
            return 'officer_visit'

        else:
            print_slow("There is a secretary at the reception desk. She looks up, and sees you by the door.")
            print_slow("Secretary: 'Can I help you with something?'")
            action = raw_input("> ")

            if action in ['yes', 'yea', 'yeah']:
                print_slow("Secretary: 'What is it? Do you have a crime to report?'")
                action = raw_input("> ")
                if action in ['yea', 'yes', 'yeah']:
                    print_slow("Secretary: 'Officer Harrigan, can you come over here please? This person would like to report a crime.'")
                    print_slow("You give your statement to the officer, selling out the baker as a purveyor of unique herbs.")
                    print_slow("What a buzz-kill.\n")
                    print_slow("You slink out of the town, people shaking their heads as you pass.")
                    print_slow("For shame.")
                    exit(0)

                elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
                    print_slow("Secretary: 'Are you sure? You look a little shifty.'")
                    print_slow("She waves to an officer nearby.")
                    print_slow("Secretary: 'Officer Harrigan, will you check this person out? Something is off with them.'\n")
                    print_slow("The officer searches you and finds your herbs.\nShe shakes her head sadly.")
                    print_slow("Officer: 'I'm going to have to confiscate these herbs, they could be dangerous in the wrong hands!'\n")
                    print_slow("She shoos you out the door.\nYou walk dejectedly out of the police station.")
                    print_slow("Better luck next time.")
                    exit(0)

                else:
                    print_slow("Secretary: 'If you're going to waste time, do it somewhere else.'")
                    print_slow("The secretary points to the door.\nYou take the hint, and leave.")
                    print_slow("You decide to quit while you're ahead, and head home with your herbs.\n")
                    print_slow("Awesome.")
                    exit(0)

            elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
                print_slow("Secretary: 'This is a police station, not a museum. Gawk somewhere else.'")
                print_slow("The secretary returns to her paperwork, dismissing you.")
                print_slow("You've had enough of the law for one day.\nTime to head home!\n")
                print_slow("Righteous.")
                exit(0)

            else:
                print_slow("Secretary: 'I can't stand a mumbler! Come back when you've learned to speak clearly.'")
                print_slow("The secretary glares at you.")
                print_slow("Startled, you back out of the police station.\n")
                print_slow("At least you have your herbs to comfort you.")
                print_slow("Tubular.")
                exit(0)

class Officer(Room):
    def enter(self):
        print_slow("Officer: 'Are you the idiot asking for Officer Greene?'")
        print_slow("You nod. She looks mad.\n")
        print_slow("Officer: 'Did the baker send you?'")
        action = raw_input("> ")

        if action in ['yes', 'yea', 'yeah']:
            print_slow("The officer rolls her eyes.")
            print_slow("Officer: 'The baker is a valuable part of our economy.'")
            print_slow("Officer: 'Forget you ever met her, and forget your way back here.'\n")
            print_slow("The officer stalks off.\n")
            print_slow("Secretary: 'That means it's time for you to go, honey.'\n")
            print_slow("You get up, shaken, and leave the station.")
            print_slow("You just wanted a brownie!")
            exit(0)

        elif action in ['no', 'nah', 'naw', 'nope', 'nevermind']:
            print_slow("Officer: 'I don't believe for a second that was just a lucky guess.'")
            print_slow("Officer: 'Whatever game you're playing, play it somewhere else.'\n")
            print_slow("The officer glares at you.\nYou stand up and leave the station.\n")
            print_slow("You can't help but feel you dodged a bullet.")
            print_slow("What a strange town.")
            exit(0)

        else:
            print_slow("Officer: 'Whatever. I don't think you're welcome in our town anymore.'")
            print_slow("Officer: 'Maybe it's time for you to leave.'\n")
            print_slow("You leave the police station, wondering what you just got yourself into.")
            print_slow("Oh well, there's a Sbux on the way home.")
            exit(0)
