import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from matplotlib.ticker import FuncFormatter, StrMethodFormatter, NullFormatter, ScalarFormatter 
from matplotlib import ticker

data = pd.read_csv("data.csv")
month = data['Month']
value = data['Value']

fig, ax = plt.subplots(figsize=(10, 10), dpi=500)

ax.tick_params(axis='x', rotation=-45) # Jobbra eldöntött x tengely jelölések
ax.yaxis.set_major_formatter(FuncFormatter(lambda value, pos: f"{int(value):,}".replace(",", "'"))) # y tengely formatálás (' elválasztó)

# halvány vonal az y tengelyről könnyebb olvashatóságért
ax.yaxis.grid(True, which='major', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
ax.set_axisbelow(True)

# Formátum (bar / line)
ax.bar(month, value,color='red',) # bar
#ax.plot(month,value,color='red', marker='o') # line

# Kiiratás
#plt.show()
plt.savefig('output.png', dpi=500)  # save the heatmap as pdf for best quality
