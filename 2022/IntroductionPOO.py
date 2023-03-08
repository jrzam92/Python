#• Position: Where is the tank?
#• Direction: In what direction is it facing?
#• Speed: How fast is it going?
#• Armor: How much armor does it have?
#• Ammo: How many shells does it have?

#OOP-speak, these actions are called methods.

#• Move: Move the tank forward.
#• Turn: Rotate the tank left/right.
#• Fire: Launch a shell.
#• Hit: This is the action when an enemy shell hits the tank.
#• Explode: Replace the tank with an explosion animation.

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)"   % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print (self.name, "has no shells!")

    def hit(self):
        self.armor -= 20
        print (self.name, "is hit!")
        if self.armor <= 0:
            self.explode()
            
    def explode(self):
        self.alive = False
        print (self.name, "explodes!")

my_tank = Tank("Bob")
my_tank.fire_at()

