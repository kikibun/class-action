# bakery adventure but with classes instead of functions
from rooms_and_class import *

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
