## Overview

We will be analyzing the Amazon product data to explore its structure as well as detect patterns and present results.

## Goals
* pandas file loading
* pandas aggregates
* pandas plotting
* matplotlib histogram
* matplotlib multiline series
* save your figures to a file
* SVG
* D3 basics

## Reading

_use these as reference as you complete the exercise_

* Python for Data Analysis: Chapter 5, 8, 9
* [Intro to Matplotlib](http://nbviewer.ipython.org/url/raw.github.com/profjsb/python-bootcamp/master/Lectures/05_NumpyMatplotlib/IntroMatplotlib.ipynb)
* [Matplotlib tutorial](matplotlib_tutorial/MatPlotLib_Tutorial.ipynb)
* [Matplotlib Reference](http://nbviewer.ipython.org/urls/raw.github.com/jrjohansson/scientific-python-lectures/master/Lecture-4-Matplotlib.ipynb)

## Assignment

### Matplotlib

For this assignment, we are going to learn how to start exploring and visualizing our data.  While inspecting data sets by hand can give some insight into the structure of the data, often you cannot see patterns unless you plot it (especially if it is high dimensional).

These visualization techniques are not just useful when presenting results and communicating your findings, but essential during the exploratory phase of your analyses.

__For this exercise, use matplotlib's object oriented API.  We also will be using inline plots in an IPython notebook__

1. Set IPython to display plots inline: `%pylab inline`

2. Load in `data/prod_1000.csv` into a pandas Dataframe.

3. Use `head()` to inspect and print out the first few rows of data.

4. To create our multi-line timeseries we first need to group by 'group' (i.e. Videos, Books, etc.).  Use pandas `[groupby()](http://pandas.pydata.org/pandas-docs/dev/groupby.html)` to aggregate our products by which product group they belong to.

5. Let us get experience with some basic grouping.  Create a [histogram](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.hist.html) of our groups to count how many of each type of product we have -- each bin should represent a different category.

6. Next we need to produce some aggregates. To display our lines we need to count how many reviews occurred on each day.  Transform the our pandas DataFrame into a new DataFrame that represents a time series mapping date => number of reviews that occured on that date. 
  * Split our grouped DataFrame so that we have a DataFrame for each of: 'Videos', 'DVD', 'Book', and 'Music'.  This will make our further analyses easier.
  * You will use `group()` to group on the date, and then [`value_counts()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html)

7. Once you have this new transformed time series, we can start having fun!  Using matplotlib's object oriented API, create a new `figure()` that is (14, 8) inches.

8. Plot each timeseries (__Videos__, __DVD__, __Book__, __Music__) on this figure: use [`plot()`](http://pandas.pydata.org/pandas-docs/dev/visualization.html) 

10. We can already start to see some trends about the distribution of certain products on Amazon.  Let us make things pretty.  Add a title and axes labels.

11. It is tough to distinguish between the lines however, add a [legend](http://matplotlib.org/users/legend_guide.html) to our plot.  If you want to get extra fancy you can add [text annotation](http://matplotlib.org/users/annotations_intro.html) on the lines as well.  

12. [Save](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig) these figures. 

### Plot High Dimensional Data

1. Now that you have some experience with basic plots in matplotlib, we can apply this knowledge to our previous recommender exercise. 

2. Reproduce Jonathan's feature vector color map.

![feature_vec](img/feature_matrix.png)

3. To do this, you will need to use two subplots.  Setup a subplot with 1 row and 2 columns.

4. Plot on the left subplot the feature vector for the 1000 product dataset.

5. Add a colorbar.

6. Repeat this process on the right sublot for the 45 product data set.

7. Add the appropriate labels and title.

8. Follow this same procedure for your similarity matrices.

![img/similarity.png]

9. Save these figures for posterity.

### Extra credit

Reproduce these plots with [D3.js](http://d3js.org/).

* [example](http://bl.ocks.org/mbostock/388495)
* [Dashing D3](https://www.dashingd3js.com/)
* [D3 Tutorial](http://alignedleft.com/tutorials/d3/)

__Call me over if you would like to start diving into D3__
