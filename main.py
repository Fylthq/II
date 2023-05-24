
class Pet:

 def __init__(self, name, species):

  self.name = name

  self.species = species

  self.hungry = True

  self.tired = True

  self.happy = False

  self.wantsrat = False

 def feed(self):

  if self.hungry:

   print(f"{self.name} has been fed.")

   self.hungry = False

   self.wantsrat = True

  else:

   print(f"{self.name} is not hungry.")

 def sleep(self):

  if self.tired:

   print(f"{self.name} has gone to sleep.")

   self.tired = False

  else:

   print(f"{self.name} is not tired.")

 def play(self):

  if self.happy:

   print(f"{self.name} is already playing.")

  else:

   print(f"{self.name} is playing now.")

   self.happy = True

 def srat(self):

  if self.wantsrat:

   print(f"{self.name} posrat")

   self.wantsrat = False

   self.hungry = True

   self.happy = True

  else:

   print(f"{self.name} doesn't want posrat")
