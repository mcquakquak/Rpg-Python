import sys
import time
import random
import pprint
import colorama
from colorama import Fore, Back
from colorama import init

init(autoreset=True)
playerAlive = True
#list of enemies
goblin = {
  "name": "Goblin",
  "health": 30,
  "attack": 7,
}


def playerCreation():
  player = {}
  player['level'] = 1
  player['xp'] = 0
  player['name'] = input(Fore.BLUE + "Whats your name? \n")
  player['xpToLevel'] = 2
  print(Fore.YELLOW + "CLASS CHOICES")
  print("(Archer   120 HP    5 DPS  (Key: 1))")
  print("(Sword     90 HP    10 DPS (Key: 2))")

  if input(Fore.YELLOW + "Whats your class? \n") == "1":
    player['class'] = "archer"
    player['max health'] = 120
    player['health'] = player['max health']
    player['atack'] = 5

  else:
    player['class'] = "sword"
    player['max health'] = 90
    player['atack'] = 10
    player['health'] = player['max health']

  return player


def spawn_enemy():
  return goblin.copy()
  '''
  Creates a copy of an enemy
  Return that enemy
  '''


def display_player(player):
  for stat, val in player.items():
    print(Fore.YELLOW + "\n" + stat + ": " + str(val))


def display_enemy(enemy):
  enemy['damage'] = 10
  enemy['health'] = 30
  for gob, val in enemy.items():
    print(Fore.RED + gob + ": " + str(val))
  '''
  Outputs the enemy stats
  Try the easy way first, and then make nice display after
  '''
  #Make it look nice, similar to display player (See if you can make the general program more efficient, maybe a general display function that can take in both enemy and player? this will replace the first 2 function)    print


def is_alive(character):
  if character['health'] <= 0:
    return False
  else:
    return True
  '''
  Check if this character (of dictionary type) is alive based on their health
  Returns True or False
  '''


def deal_damage(enemy):
  enemy['health'] -= player['atack']
  print(Fore.RED + "enemy health: " + enemy['health'])
  '''
  Have the player and enemy attack each other once
  The player attacks first
  The enemy only attacks if it is still alive
  This should affect the health of the characters
  '''


def player_attack(enemy):
  if input("Do you want to atack Yes(1) No(2)") == 2:
    player['health'] -= enemy['attack']
    print(Fore.GREEN + player['health'])
  else:
    enemy['health'] -= player['atack']
    print(Fore.GREEN + "player health: " + str(player['health']))
    print(Fore.RED + "enemy health: " + str(enemy['health']))
  '''
  Have the player attack the enemy o1ne time
  This should affect the enemy's health
  Add prints to show what is happening
  '''


def enemy_attack(enemy):
  player['health'] -= enemy['damage']
  '''
  Have the enemy attack the player one time
  This should affect the player's health
  Add prints to show what is happening
  '''


def enemy_defeated():
  player['xp'] += 1
  '''
  Reward the player with 1 xp when the enemy is defeated
  You can adapt this to give other rewards later
  '''


def level_up():
  if player['xp'] >= player['xpToLevel']:
    player['xpToLevel'] += 1
    player['level'] += 1
    player['xp'] = 0
    player['atack'] += 1
    player['max health'] += 3
    player['health'] == player['max health']
  '''
  Check if the player has 10 or more xp points to level up
  If leveled up, increase the player's stats and reset the xp points
  An increase of 1 or 2 is good to start
  '''


def town():
  player['health'] = player['max health']
  '''
  Reset the player's health based on their max health
  '''


#Fight Loop
def fight(player):
  global playerAlive
  enemy = spawn_enemy()
  display_enemy(enemy)
  while is_alive(player) and is_alive(enemy):
    player_attack(enemy)
    if is_alive(enemy):
      enemy_attack(enemy)
  if not is_alive(enemy):
    enemy_defeated()
    level_up()
  if not is_alive(player):
    playerAlive = False


# print("Whats your name: ")
# name = input()
# player['name'] = name
# print("Welcome adventurer," + player["name"] + "!")

player = playerCreation()

#Main Game Loop
while playerAlive:
  display_player(player)
  print(Fore.BLACK + "1 - Fight and enemy")
  print(Fore.MAGENTA + "2 - Go to town")
  choice = input("Choose an option ")
  if choice == "1":
    fight(player)
  elif choice == "2":
    print(Fore.LIGHTBLUE_EX + "You went to town and regained your health")
    town()
  else:
    print("Invalid Choice.")

print("Your adventure has ended.")
