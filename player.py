from model.weapon import *

class Cat:
   
   def __init__(self, pseudo, classe):
      self.pseudo = pseudo
      self.classe = classe
      self.weapon = None
         
      if self.classe == "Tank":
         self.health = 140
         self.attackdmg = 3
      elif self.classe == "Guerrier":
         self.health = 100
         self.attackdmg = 5
      elif self.classe == "Mage":
         self.health = 80
         self.attackdmg = 8      
      
   def get_pseudo(self):
      return self.pseudo 
   def get_classe(self):
      return self.pseudo 
   def get_health(self):
      return self.pseudo  
   def get_attackdmg(self):
      return self.attackdmg

   def damage(self, damage):
      if damage + Weapon.get_damage(self) >= self.health + Shield.get_shieldpower(self):
         self.health = 0
         print("Votre chat est mort...")
      else:
         self.health -= damage - Weapon.get_damage(self) + Shield.get_shieldpower(self)
         print("Votre chat a subit", damage, "dégats.")
         print("Vous avez désormais", self.health, "points de vie.\n")
         
   def attack_player(self, targeted_cat):
      targeted_cat.damage(self.attackdmg)
      print("Vous attaquez le chat", targeted_cat, "!")
      print("Vous lui avez infligé", self.attackdmg, "dégats !")
      print(targeted_cat, "n'a plus que", targeted_cat.self.health)