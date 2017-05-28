# bakery adventure but with classes instead of functions
nosy_counter = 0
police_officer = False

class Room(object):
    def enter(self):
#        #this is where room text goes
        pass

class GameEngine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class TownSquare(Room):
    def enter(self):
        print "You are in the center of a small town. \n Ahead, you see a bakery, a butcher, and a police station."
        print "You decide to look around. \n Which do you enter first?"
        action = raw_input("> ")

        if action == "bakery":
            print "You approach the bakery. It is evident the baker has been busy!"
            return 'bakery_room'

        elif action == "butcher":
            print "You start to approach the butcher, but he looks kind of mean. \n Maybe you will come back later."
            return 'town_square'

        elif action == "police station":
            print "For a sleepy little town, there sure is a large police station. \n You wonder how many officers are staffed."
            print "Thinking about that makes you hungry. You always get hungry when you're nervous."
            return 'town_square'

class Map(object):
    rooms = {'town_square' : TownSquare()}

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
