import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from matplotlib.ticker import FuncFormatter, StrMethodFormatter, NullFormatter, ScalarFormatter 
from matplotlib import ticker

# Adatok beolvasása (Month / Value oszlopok)
data = pd.read_csv("data.csv")
x = data['Month']
y = data['Value']

# Diagram készítése
fig, ax = plt.subplots()

# Beállítások
ax.tick_params(axis='x', rotation=-45) # Jobbra eldöntött x tengely jelölések
plt.tight_layout() # szélesebb margó
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "'"))) # y tengely formatálás (' elválasztó)

# halvány vonal az y tengelyről könnyebb olvashatóságért
ax.yaxis.grid(True, which='major', color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
ax.set_axisbelow(True)

# Formátum (bar / line)
ax.bar(x, y,color='red') # bar
#ax.plot(x,y,color='red', marker='o') # line

# Kiiratás
plt.show()
