img_array = X[36000]
img_array_reshaped=img_array.reshape(28, 28)
plt.imshow(img_array_reshaped, cmap = mpl.cm.binary,
           interpolation="nearest")
plt.axis("off")
save_fig("img_plot")
plt.show()

#define
def plot_digit(img_array):
    img_array_reshaped = img_array.reshape(28, 28)
    plt.imshow(img_array_reshaped, cmap = mpl.cm.binary,
               interpolation="nearest")
    plt.axis("off")