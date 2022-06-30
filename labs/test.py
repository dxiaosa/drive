
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(f"dataset/021_1min_seg.csv")

# draw line plot of amount
f = plt.figure(1, figsize=(16, 20))

ax = f.add_subplot(len(df.keys()),1,1)
plt.boxplot(df['eda_avg'].values)
ax.set_ylim((df['eda_avg'].min(), df['eda_avg'].max()))
f.canvas.draw()

# i=1
# for string in df.keys():
#     if (string not in ['local_time']):
    
#         axis = f.add_subplot(len(df.keys()),1,i)
#         axis.boxplot(df[string])
#         axis.title.set_text(string + " - Box plot")
#         i+=1

plt.show()