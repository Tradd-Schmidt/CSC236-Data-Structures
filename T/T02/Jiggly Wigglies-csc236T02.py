def player_count():
   ''' Asks user(s) how many players will play the game'''
   player_num = int(input('Between 1 to 4, how many number of players will play this game? '))
   print (str(player_num) + " player(s) will be playing this game!" )#prints the number
   return player_num

import random   # This is needed later in the program to do our dice rolling
def get_body_part():
   """
   Will generate a random integer to simulate the rolling of a die and will return the corresponding body part to the
   resulting number
   Pre: none
   Post: an all lowercase string
   :return: an all lowercase string
   """

   l = ["body", "head", "legs", "eyes", "feelers", "tail"]  # This is a list that contains all the body parts that can be rolled for in order of 0-5
   x = random.randint(0, 5)    # This uses random to choose an integer 0-5 which will simulate the die roll
   if x == 2 or x == 3 or x == 4:
       print("A pair of " + l[x] + " were rolled.")
   else:
       print("A " + l[x] + " was rolled.")

   return l[x]     # This is to return whatever corresponding body part was received after the rolling of the die

def check_progress(player):
   """
       Will print out the count of body parts that the current
   player has.
       Pre: player is a dictionary for whoever’s turn it
   is, and this dictionary contains all the keys already set
   necessary for all the body parts.
       Post: Prints out the current count of each body part for
    the current player and returns a boolean depending on if the
    player has won or not.
    """
   print("active player currently has " + str(player['body']) +
         " body piece(s), " + str(player["legs"]) + " pair(s) of legs, "
         + str(player["head"]) + " head piece(s), "
         + str(player["eyes"]) + " eyes, " + str(player["feelers"])
         + " feeler(s), and " + str(player['tail']) + 'tail.')
   if player['body'] == 1 and player['legs'] == 3 and player['head'] == 1\
           and player['eyes'] == 2 and player['feelers'] == 2 and player['tail'] == 1:
       return True
   else:
       return False



def add_body_part(player, bodypart):
   """
   Will check a player’s list of body parts already obtained,
   and if the part that was input can be added to the dictionary, it is added.

   Pre: player is a dictionary for whoever’s turn it is,
   and this dictionary contains all the keys already set necessary for all the body parts.
   body_part is an all lowercase string which is
   the body part that is being added to a specific player’s bug.

   Post: If the body part was able to be added,
   the dictionary key corresponding to that body part will be changed.
   Otherwise the dictionary is not altered.
   """
   requirelist = {"body":"none",
                  "head":"body",
                  "tail":"body",
                  "legs":"body",
                  "feelers":"head",
                  "eyes":"head"}

   maxcount = {"body":1,
               "head":1,
               "tail":1,
               "legs":3,
               "feelers":2,
               "eyes":2}

   currcount = player[bodypart]
   currmax = maxcount[bodypart]
   requiredpart = requirelist[bodypart]

   if currcount < currmax:
       if requiredpart == "none":
           player[bodypart] += 1
           print("Player now has " + str(player[bodypart]) +" "+ str(bodypart) + "(s).")
           return
       elif player[requiredpart] > 0:
           player[bodypart] += 1
           print("Player now has " + str(player[bodypart]) +" "+ str(bodypart) + "(s).")
           return
   print("The body part couldnt be added.")

def main():
   """Plays the game of Beetle"""
   print("Lets play a game of Beetle")

   playernumber = player_count()

   players = []

   for dummy_i in range(playernumber):
       players.append({"body":0,
                       "head":0,
                       "tail":0,
                       "legs":0,
                       "feelers":0,
                       "eyes":0})

   nowinner = True
   while nowinner:
       for count, player in enumerate(players):

           print("It is now player " + str(count%len(players) + 1)+ "s turn.")
           add_body_part(player, get_body_part()) # no need to keep the roll.
           if check_progress(player): # dont need to print state, check_progress handles it.
               nowinner = False
               break

if __name__ == '__main__':
    main()