from random import random

computer_pick_list = ['rock','paper','scissors']
random_val = round(random()*2)
computer_pick = computer_pick_list[random_val]

print(computer_pick)