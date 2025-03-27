import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('datalab.csv')
# df.plot() # graphic lines
df.plot(kind='scatter', x='Duration',y='Maxpulse')  # seeds graphic

plt.show()