"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    """
    The Character defaults to implementing some of its hook methods with the
    following standard functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead)
    at_after_move - launches the "look" command
    at_post_puppet(player) -  when Player disconnects from the Character, we
                    store the current location, so the "unconnected" character
                    object does not need to stay on grid but can be given a
                    None-location while offline.
    at_pre_puppet - just before Player re-connects, retrieves the character's
                    old location and puts it back on the grid with a "charname
                    has connected" message echoed to the room

    """
    def at_object_creation(self):
        "Called only when first created"
        
        self.db.name = ''
        self.db.birthday = ''
        self.db.age = ''
        self.db.sex = ''
        
        self.db.order = ''
        self.db.path = ''
        
        # Gaining spells/attributes/abilities after 
        # the creation of the character
        self.db.votes = 0
        self.db.xp = 0

        # Attributes

        # Mental
        self.db.intelligence = 0
        self.db.wits = 0
        self.db.resolve = 0

        # Physical
        self.db.strength = 0
        self.db.dexterity = 0
        self.db.stamina = 0

        # Social
        self.db.presence = 0
        self.db.manipulation = 0
        self.db.composure = 0

        # Abilities
         
        # Mental
         self.db.academics = 0
         self.db.computers = 0
         self.db.crafts = 0
         self.db.investigation = 0
         self.db.medicine = 0
         self.db.occult = 0
         self.db.politics = 0
         self.db.science = 0

         # Physical
         self.db.athletics = 0
         self.db.brawl = 0
         self.db.driving = 0
         self.db.flying = 0 # for booms and quidditch
         self.db.firearms = 0 # crossbows and other ranged weapons
         self.db.dueling = 0 # wizarding dueling
         self.db.larceny = 0
         self.db.stealth = 0
         self.db.survival = 0
         self.db.weaponry =  0

         # Social
         self.db.animalken = 0
         self.db.empathy = 0
         self.db.expression = 0
         self.db.intimidation = 0
         self.db.persausion = 0
         self.db.socialize = 0
         self.db.streetwise = 0
         self.db.subterfuge = 0

        #Combat related
        self.db.size = 0
        self.db.speed = 0
        self.db.initiative_mod = 0
        self.db.defense = 0
        self.db.armor = 0

        self.db.health = 1
        self.db.willpower = 0

        self.db.merits = []
        self.db.flaws = []
