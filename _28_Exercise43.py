from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter",
        "Such a luser",
        "I have a small puppy that's better at this."
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an")
        print("escape pod.")
        print("\n")
        print("Your are running down the central corridor to the Weapons Armory when")
        print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")
        
        action = input('> ')

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            return 'death'
        elif action == "dodge!":
            print("Like a world class boxer")
            return 'death'
        elif action == "tell a joke!":
            print("Lucky for your")
            return 'laser_weapon_armory'
        else:
            print("Does not compute")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("You do a dive roll into the armory room. The code is 3 digit")
        code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDD")
            guesses += 1
            guess = input("[Keypad]> ")

        if guess == code:
            print("The container clicks open and the seal breaks.")
            return 'the_bridge'
        else:
            print("You are dead")
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("You burst onto the bridge.")

        action = input("> ")

        if action == "throw the bomb":
            print("You throw the bomb")
            return 'death'
        elif action == "slowly place the bomb":
            print("point your blasteer at the bomb")
            return 'escape_pod'
        else:
            print("does not compute")
            return "the bridge"

class EscapePod(Scene):
    def enter(self):
        print("You rush through the ship")

        good_pod = randint(1,5)
        guess = input("[pid #]>")

        if int(guess) != good_pod:
            print("You are dead")
            return 'death'
        else:
            print("You jumped in correct one")
            return 'finished'

class Map(object):
    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'death' : Death()      
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()