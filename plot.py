#!/usr/bin/env python

#draw normal distribution
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x = list(range(-10,10,1))
x_mean = np.mean(x)
x_std = np.std(x)
y = stats.norm.pdf(x, x_mean, x_std)
plt.plot(x, y) # including h here is crucial

# save plot
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)#core codeline

#draw from df - scatter

# hist 
%matplotlib inline
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
save_fig("attribute_histogram_plots")
plt.show()

# 2-dim y and x1
housing.plot(kind="scatter", x="median_income", y="median_house_value",
             alpha=0.1)
plt.axis([0, 16, 0, 550000])#xmin, xmax, ymin, ymax
save_fig("income_vs_house_value_scatterplot")

# 2-dim info
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
save_fig("better_visualization_plot")

#draw out a map if you have longitude and latitude
# 4-dim info
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
    s=housing["population"]/100, label="population", figsize=(10,7),
    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
    sharex=False)
plt.legend()

