

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data_sofi.csv')
corr = df.corr().abs()
mask = np.triu(corr)
cmap = sns.diverging_palette(150, 10, as_cmap=True)
plt.figure(figsize = (15,10))
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=0.75, center=0.2, annot = True, fmt = '.2f', square=True, linewidths=.5).set_title("Correlation")

df2 = pd.read_csv('data_sofi2.csv')
corr = df2.corr().abs()
mask = np.triu(corr)
cmap = sns.diverging_palette(150, 10, as_cmap=True)
plt.figure(figsize = (15,10))
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=0.75, center=0.2, annot = True, fmt = '.2f', square=True, linewidths=.5).set_title("Correlation")