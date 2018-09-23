from datascience import  *
from math import *
gain = {}
def entropy():
    return  -class_yes * log2(class_yes) - class_no * log2(class_no)

def for_outlook():
    p_sunny_rows = inputter.where('outlook', 'sunny').num_rows
    p_sunny = p_sunny_rows / a
    p_sunny_yes = inputter.where('outlook', 'sunny')
    p_sunny_yes = p_sunny_yes.where('play tennis', 'yes').num_rows
    p_sunny_yes = p_sunny_yes / p_sunny_rows
    p_sunny_no = 1 - p_sunny_yes
    p_sunny_cal = p_sunny * ((- p_sunny_yes * (log2(p_sunny_yes))) - (p_sunny_no * (log2(p_sunny_no))))

    p_overcast_rows = inputter.select('outlook').where('outlook', 'overcast').num_rows
    p_overcast = p_overcast_rows / a
    p_overcast_yes = inputter.where('outlook', 'overcast')
    p_overcast_yes = p_overcast_yes.where('play tennis', 'yes').num_rows
    p_overcast_yes = p_overcast_yes / p_overcast_rows
    p_overcast_no = 1 - p_overcast_yes
    p_overcast_cal = p_overcast * ((- p_overcast_yes * (log2(p_overcast_yes))))

    p_rain_rows = inputter.select('outlook').where('outlook', 'rain').num_rows
    p_rain = p_rain_rows / a
    p_rain_yes = inputter.where('outlook', 'rain')
    p_rain_yes = p_rain_yes.where('play tennis', 'yes').num_rows
    p_rain_yes = p_rain_yes / p_rain_rows
    p_rain_no = 1 - p_rain_yes
    p_rain_cal = p_rain * ((- p_rain_yes * (log2(p_rain_yes))) - (p_rain_no * (log2(p_rain_no))))

    fo = p_sunny_cal + p_overcast_cal + p_rain_cal
    outlook_gain = entropy_val - fo
    print("gain for outlook is: " +str(outlook_gain))
    gain['outlook'] = [outlook_gain]


def for_temperature():
    p_hot_rows = inputter.where('temperature', 'hot').num_rows
    p_sunny = p_hot_rows / a
    p_hot_yes = inputter.where('temperature', 'hot')
    p_hot_yes = p_hot_yes.where('play tennis', 'yes').num_rows
    p_hot_yes = p_hot_yes / p_hot_rows
    p_hot_no = 1 - p_hot_yes
    p_hot_cal = p_sunny * ((- p_hot_yes * (log2(p_hot_yes))) - (p_hot_no * (log2(p_hot_no))))

    p_mild_rows = inputter.select('temperature').where('temperature', 'mild').num_rows
    p_mild = p_mild_rows / a
    p_mild_yes = inputter.where('outlook', 'overcast')
    p_mild_yes = p_mild_yes.where('play tennis', 'yes').num_rows
    p_mild_yes = p_mild_yes / p_mild_rows
    p_mild_no = 1 - p_mild_yes
    p_mild_cal = p_mild * ((- p_mild_yes * (log2(p_mild_yes))) - (p_mild_no * (log2(p_mild_no))))

    p_cool_rows = inputter.select('temperature').where('temperature', 'cool').num_rows
    p_cool = p_cool_rows / a
    p_cool_yes = inputter.where('temperature', 'cool')
    p_cool_yes = p_cool_yes.where('play tennis', 'yes').num_rows
    p_cool_yes = p_cool_yes / p_cool_rows
    p_cool_no = 1 - p_cool_yes
    p_cool_cal = p_cool * ((- p_cool_yes * (log2(p_cool_yes))) - (p_cool_no * (log2(p_cool_no))))

    ft = p_hot_cal + p_mild_cal + p_cool_cal
    temperature_gain = entropy_val - ft
    print("gain for temperature is: " + str(temperature_gain))
    gain['temperature'] = [temperature_gain]


def for_humidity():
    p_high_rows = inputter.where('humidity', 'high').num_rows
    p_high = p_high_rows / a
    p_high_yes = inputter.where('humidity', 'high')
    p_high_yes = p_high_yes.where('play tennis', 'yes').num_rows
    p_high_yes = p_high_yes / p_high_rows
    p_high_no = 1 - p_high_yes
    p_high_cal = p_high * ((- p_high_yes * (log2(p_high_yes))) - (p_high_no * (log2(p_high_no))))

    P_normal_rows = inputter.select('humidity').where('humidity', 'normal').num_rows
    p_normal = P_normal_rows / a
    p_normal_yes = inputter.where('humidity', 'normal')
    p_normal_yes = p_normal_yes.where('play tennis', 'yes').num_rows
    p_normal_yes = p_normal_yes / P_normal_rows
    p_normal_no = 1 - p_normal_yes
    p_normal_cal = p_normal * ((- p_normal_yes * (log2(p_normal_yes))) - (p_normal_no * (log2(p_normal_no))))

    fh = p_high_cal + p_normal_cal
    humidity_gain = entropy_val - fh
    print("gain for humidity is: " + str(humidity_gain))
    gain['humidity'] = [humidity_gain]

def for_wind():
    p_weak_rows = inputter.where('wind', 'weak').num_rows
    p_weak = p_weak_rows / a
    p_weak_yes = inputter.where('wind', 'weak')
    p_weak_yes = p_weak_yes.where('play tennis', 'yes').num_rows
    p_weak_yes = p_weak_yes / p_weak_rows
    p_weak_no = 1 - p_weak_yes
    p_weak_cal = p_weak * ((- p_weak_yes * (log2(p_weak_yes))) - (p_weak_no * (log2(p_weak_no))))

    p_strong_rows = inputter.select('wind').where('wind', 'strong').num_rows
    p_strong = p_strong_rows / a
    p_strong_yes = inputter.where('wind', 'strong')
    p_strong_yes = p_strong_yes.where('play tennis', 'yes').num_rows
    p_strong_yes = p_strong_yes / p_strong_rows
    p_strong_no = 1 - p_strong_yes
    p_strong_cal = p_strong * ((- p_strong_yes * (log2(p_strong_yes))) - (p_strong_no * (log2(p_strong_no))))

    fw = p_weak_cal + p_strong_cal
    wind_gain = entropy_val - fw
    print("gain for wind is: " + str(wind_gain))
    gain['wind'] = [wind_gain]

inputter = Table.read_table('tennis.csv')
print("our main class is PLAY TENNIS")
print("sub-classes are YES and NO")
a = inputter.num_rows
class_yes = inputter.select('play tennis').where('play tennis', 'yes').num_rows
class_yes = class_yes / a
class_no = 1 - class_yes
print("probability of class YES is: "+str(class_yes))
print("probability of class NO is: "+str(class_no))
entropy_val = entropy()
print("Entropy value is: " +str(entropy_val))
for_outlook()
for_temperature()
for_humidity()
for_wind()
root = max(gain, key=gain.get)
print("Root of the decision tree is: " +str(root))