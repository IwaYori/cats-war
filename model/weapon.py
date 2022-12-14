class Weapon:
   
   def __init__(self, name, damage):
      self.name = name
      self.damage = damage
      
   def get_name(self):
      return self.name
   def get_damage(self):
      return self.damage
   
class Shield:
   
   def __init__(self, name, shield):
      self.name = name
      self.shield = shield
      
   def get_name(self):
      return self.name
   def get_shieldpower(self):
      return self.shield