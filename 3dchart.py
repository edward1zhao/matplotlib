import pandas as pd
import numpy as np
import matplotlib
import matplotlib.style
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("seaborn-muted")

df = pd.read_csv("Optimize.csv").iloc[:, :-1]
data = df.values

columns = df.columns.tolist()
def get_lims(l):
    return (np.min(l), np.max(l))

color_map = cm.jet


fig = plt.figure(figsize=(20, 10))
ax = fig.gca(projection='3d')
ax.xaxis._axinfo['label']['space_factor'] = 10

ax.plot_trisurf(data[:, 2], data[:, 1], data[:, 0], cmap=cm.jet, linewidth=0.1, antialiased=True, edgecolor="black", shade=True)

ax.set_xlabel(columns[2],fontsize=20)
ax.set_ylabel(columns[1],fontsize=20)
ax.set_zlabel(columns[0],fontsize=20)


ax.set_xlim(get_lims(data[:, 2]))
ax.set_ylim(get_lims(data[:, 1]))
ax.set_zlim(get_lims(data[:, 0]))

ax.set_xticks(np.arange(np.min(data[:, 2]), np.max(data[:, 2]), 1))
ax.set_xticklabels(map(lambda x: "{:.0f}".format(x), np.arange(np.min(data[:, 2]), np.max(data[:, 2]), 1)), fontsize=10)

ax.set_yticks(np.arange(0.1, 1, 0.1))
ax.set_yticklabels(map(lambda x: "{:.2f}".format(x), np.arange(0.1, 1, 0.1)), fontsize=10)

ax.set_zticks(np.arange(0, np.max(data[:, 0]), 0.2))
ax.set_zticklabels(map(lambda x: "{:.1f}".format(x), np.arange(0, np.max(data[:, 0]), 0.2)), fontsize=10)

ax.view_init(50, -20)

ax.xaxis.labelpad=30
ax.yaxis.labelpad=30



plt.show()
