from datascience import  *
from math import *

def entropy():
    return  -class_yes * log2(class_yes) - class_no * log2(class_no)

def for_outlook():
    p_sunny = inputter.select('outlook').where('outlook', 'sunny').num_rows
    p_sunny = p_sunny / a
    p_sunny_yes = inputter.where('outlook', 'sunny').where()
    p_sunny_yes = p_sunny_yes.where('play tennis', 'yes')
    #p_sunny_yes = p_sunny_yes / p_sunny
    print(p_sunny_yes)

    p_overcast = inputter.select('outlook').where('outlook', 'sunny').num_rows
    p_overcast = p_overcast / a

    p_rain = inputter.select('outlook').where('outlook', 'sunny').num_rows
    p_rain = p_rain / a

inputter = Table.read_table('tennis.csv')
print("our main class is PLAY TENNIS")
print("sub-classes are YES and NO")
a = inputter.num_rows
class_yes = inputter.select('play tennis').where('play tennis', 'yes').num_rows
class_yes = class_yes / a
class_no = 1 - class_yes
print("probability of class YES is: "+str(class_yes))
print("probability of class NO is: "+str(class_no))
entropy = entropy()
print(entropy)
for_outlook()
