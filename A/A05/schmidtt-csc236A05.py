#############################################################################################
# Name: schmidtt-csc236A05
# Author: Tradd Schmidt
#
# Purpose: To allow a user to interact with a pet and allow it to play with a toy
#
#############################################################################################

import time

from Pet import Pet
from Toy import Toy


def let_pet_play(pet):
    """
    This is a prompt to allow the user to interact with the pet and let it play with the toy. It additionally keeps
    track of how long it took for the pet to be allowed to play with the toy and decreases the pet happiness
    accordingly.
    :param pet: The pet that is being allowed to play
    :return: none
    """
    t_1 = time.time()
    input("Press enter to allow your pet to play with it's toy.")
    t_2 = time.time()
    t = t_2 - t_1       # Calculates how long it took for the user to press enter
    pet.happiness -= t


def main():
    new_pet = Pet()
    new_toy = Toy()
    let_pet_play(new_pet)
    new_pet.idle()
    while new_pet.alive:
        if new_pet.energy == 0:         # Checks to make sure the pet has the energy to play with the toy
            print("Your pet is too tired and needs to sleep for 60 seconds.")
            new_pet.sleep()
            let_pet_play(new_pet)
            new_pet.idle()
        elif new_toy.battery_power == 0:    # Checks to make sure the toy has the battery level to play
            print("It looks like the toy's battery is dead. You will have to wait 35 seconds for the battery to "
                  "recharge.")
            new_toy.charge_battery()
            let_pet_play(new_pet)
            new_pet.idle()
        elif new_pet.energy > 0:
            if new_pet.energy <= new_toy.battery_power:     # If the toy has more battery power than the pet has energy,
                time.sleep(new_pet.energy)                  # the pet energy and toy battery life are decreased by the
                new_toy.drain_battery(new_pet.energy)       # pet energy level
                new_pet.play_with_toy(new_pet.energy)
                let_pet_play(new_pet)
                new_pet.idle()
            else:
                time.sleep(new_toy.battery_power)               # If the pet has more energy than the toy has battery,
                new_pet.play_with_toy(new_toy.battery_power)    # the pet energy and toy battery life are decreased by
                new_toy.drain_battery(new_toy.battery_power)    # the battery power
                let_pet_play(new_pet)
                new_pet.idle()
    print("Oh no! It seems your pet got too unhappy and died. Try not to wait too long to let it play next time.")
    # If a user takes too long, the pet dies
if __name__ == "__main__":
    main()
