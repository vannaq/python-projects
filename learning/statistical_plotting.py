#adding error bars to bar charts tell us something about the distribution of data
#each call to the ax.bar method takes an x argument and a y argument so one way to do error bars is to use the yerr keyword argument: yerr=df['col'].std() or .mean()
#   ax.bar("name", df['col'].mean(), yerr=df['col'].std())
#error bars can be added to line plots, bar charts, histograms, boxplots

#adding boxplots: ax.boxplot([df['col'], df2['col2']])
#adding error bars to a plot: ax.errorbar(df['col'], df['col2'], yerr=df['col3'])


#scatterplots: ax.scatter(df['col'], df['col2])
#encoding third variable by color using c keyword argument: c=df.index -- note this is not the color argument, just the letter c


#styling plots to share with others: plt.style.use("ggplot")
#default style: plt.style.use("default")


#to save figure to file: fig.savefig("filename.ext")
#   use different extensions for different file formats
#   control resolution, or quality of image, by using dpi=number (the higher the number, the higher the quality)
#to control size of figure: fig.set_size_inches([width, height])
