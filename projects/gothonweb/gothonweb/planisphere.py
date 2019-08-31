class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body. He's blocking the door to 
the Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made yu learn Gothon insults in thee academy. You
tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgh
nebhaq. The Gothon stops, tries
not to laugh, then busts out laughing and can't move. While he's
laughing you run up and shoot him square in the head putting him down
""")

the_bridge = Room("The Bridge",
"""The container
""")

escape_pod = Room("Escape Pod",
"""You point your blaster
""")

the_end_winner = Room("The End",
"""You jump into the pod
""")

the_end_loser = Room("The End",
"""You jump into a random
""")

escape_pod.add_paths({
    '2' : the_end_winner,
    '*' : the_end_loser
})

generic_death = Room("death", "You died")

the_bridge.add_paths({
    '0132' : the_bridge,
    '*' : generic_death
})

central_corridor.add_paths({
    'shoot' : generic_death,
    'dodge' : generic_death,
    'tell a joke' : laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential problem
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible problem
    """
    for key, value in globals().items():
        if value == room:
            return key