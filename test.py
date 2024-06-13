import random as rand


number_of_plain_balls = rand.randint(1,50)
coloured_balls_list = []



for each_plain_ball in range(0 ,(number_of_plain_balls)+1):
    choice_of_colour_for_plain_balls = rand.choice(['Red','Blue','Green'])          
    coloured_balls_list.append(choice_of_colour_for_plain_balls)                        

print(coloured_balls_list)

dictionary_to_maintain_the_counter_of_colour = {'Red' :0 , 'Green' : 0 , 'Blue' : 0}
for each_coloured_ball in coloured_balls_list:
    dictionary_to_maintain_the_counter_of_colour[each_coloured_ball] += 1
print(dictionary_to_maintain_the_counter_of_colour)

