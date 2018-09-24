import tkinter as tk
from tkinter import filedialog
from datascience import *
from pandas import *
import numpy as np
from math import log2

root = tk.Tk()

file_path = filedialog.askopenfilename()
file = Table.read_table(file_path)
a = Table.read_table(file_path)
e = pandas.read_csv(file_path, header = 0)
c = a.num_rows
column_names = a.labels
print("Column names in your csv are: ")
i = 1
for x in range(0, len(column_names)):
    print(str(i)+ ".", column_names[x])
    i+=1

clas = int(input("select the column to be selected as class: "))
#uniq contains unique values in our class
uniq = e[column_names[clas - 1]].unique()
# p_class will contain probabilities of values in our selected class column
p_class = []
for y in range(0, len(uniq)):
    clas1 = a.select(column_names[clas - 1]).where(column_names[clas - 1], uniq[y]).num_rows
    clas1 = clas1 / c
    p_class.append(clas1)
print(p_class)

def ent(list):
    entropy, g = 0, 0
    for z in list:
        entropy += - list[g] * log2(list[g])
    return entropy







