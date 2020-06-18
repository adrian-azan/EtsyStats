import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = pd.DataFrame(data1,columns=['Country','GDP_Per_Capita'])

print(df1)


root = tk.Tk()

figure1 = plt.Figure(figsize=(6,5), dpi = 100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack()
df1.plot(kind='bar',legend=True, ax=ax1)


root.mainloop()