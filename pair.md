# Exploring real Health Care data using Pandas  

You are a rogue data scientist living in the hood of South Brooklyn. The streets are bad enough, but what is worse is the health conditions of the projects.
Your neighbor, who introduced himself as Bling, has been missing for the last week. Upon his return, he tells you he's been in the hospital for *Viral Meningitis*.
That's when his brother, Bundles, begins showing symptoms of *Viral Meningitis*. Bling asks you to help him find the best hospital to go to for the least amount of cash money.


### The first goal of this sprint is to find which hospital charges the most for treating *Viral Meningitis*.
We will be using the data file `hospital-costs.csv` located in the data folder.

Here is how to start off.  

```python
import pandas as pd

df = pd.read_csv("data/hospital-costs.csv")
````
1.  Now, look at and familiarize yourself with the dataset you will be working with.  
2.  Keep the official pandas documentation handy and apply generously as needed. http://pandas.pydata.org/pandas-docs/stable/
<br>

The amount in the charge/costs columns is the price per discharge. Most hospitals treat many people with the same illness.  The amount they treat is the number in the "Discharges" column.
<br>
### It is your job to calculate all the cost totals.
1. Create a new column "Total Charges" using "Discharges" and "Mean Charge".  
2. Do the same for the "Total Costs" using "Mean Cost".
2. With these two new "Total Charges" and "Total Costs" columns, calculate the charges to costs "markup" rate.
3. Tell me which procedure has the highest "markup" rate, and which one has the lowest "markup" rate.  (It's always good to do a sanity check, do these results make sense to you?)

Results:

#### Lowest
| Facility Name | ... | Total Charge | Total Cost | Markup|
| ------------- |---|:-------------:| -----:|------|
|TLC Health Network Tri-County Memorial Hospital | ...|  1540540    | 97482510  | 0.015803|

#### Highest
| Facility Name | ... | Total Charge | Total Cost | Markup|
| ------------- |---|:-------------:| -----:|------|
| SUNY Downstate Medical Center at LICH | ... | 43088   | 2068  | 20.835590|

<br>

# Out of curiosity...
I wonder what everyone is going to the hospital for...
Use a groupby method on the Description column and sum the Discharges.

1.  What are the top 10 reasons people are going to the hospital for, and how many people did they see.

# Now, lets follow the money...
Now we want to see which hospital has the most money coming.
To keep this from getting messy, lets create a new DataFrame with only the columns we care about.  
*  Create a new DataFrame named "net" that is only the Facility Name, Total Charge, Total Cost from our original DataFrame  
*  Find the total amount each hospital spent, and how much they charged. (Group your data by Facility names, and sum all the total costs and total charges)
*  Now find the net income for every hospital. Tell me the most profitable and the least profitable ones and how much are they making?


| Facility Name | Total Charge | Total Cost | Net Income |
|---|---|---|---|
| Adirondack Medical Center-Saranac Lake Site|141573499.0|77427664.0|64145835.0 |
| Albany Medical Center - South Clinical Campus|1802808.0|1432784.0|370024.0 |
| Albany Medical Center Hospital|3763945310.0|1336298908.0|2427646402.0 |
| Albany Memorial Hospital|221974029.0|94907174.0|127066855.0 |

<br>


# Now, lets focus in on *Viral Meningitis*
1. Create a new dataframe that only contains the data corresponding to *Viral Meningitis*  
	```python
	newdf = df[df["Illness"] == "Viral Meningitis"]]
	```
2. Now, with our new dataframe, only keep the data columns we care about which are:  
`["Facility Name", "APR DRG Description","APR Severity of Illness Description","Discharges", "Mean Charge", "Median Charge", "Mean Cost"]`
<br>

3. Our new dataframe should look somewhat like this:

|Facility Name|APR DRG Description|APR Severity of Illness Description|Discharges|Mean Charge|Median Charge|Mean Cost|
|----|----|----|----|----|----|----|
|Adirondack Medical Center-Saranac Lake Site|Viral Meningitis|Minor|1|17116.0|17116.0|7006.0|
|Albany Medical Center Hospital|Viral Meningitis|Minor|19|13212.0|11914.0|4569.0|
|Albany Medical Center Hospital|Viral Meningitis|Moderate|11|21197.0|14197.0|7131.0|
|Albany Medical Center Hospital|Viral Meningitis|Major|6|28074.0|22846.0|7495.0|
---

<br>

3. Find which hospital is the least expensive for treating Moderate cases of VM. [*note example below is the most expensive not the least*]


|Facility Name|APR DRG Description|APR Severity of Illness Description|Discharges|Mean Charge|Median Charge|Mean Cost|
|----|----|----|----|----|----|----|
|Beth Israel Med Center-Kings Hwy Div|Viral Meningitis|Moderate|1|71663.0|71663.0|12658.0|
|Lutheran Medical Center|Viral Meningitis|Moderate|2|71850.0|71850.0|50605.0|
|New York Presbyterian Hospital - Downtown Division|Viral Meningitis|Moderate|1|76528.0|76528.0|27563.0|
|St Lukes Roosevelt Hospital - St Lukes Hospital Division|Viral Meningitis|Moderate|4|79245.0|48006.0|24743.0|
|Orange Regional Medical Center|Viral Meningitis|Moderate|1|84003.0|84003.0|23143.0|
---
<br>

4. Find which hospital is the least expensive for treating Moderate cases of VM **that have at least 3 or more Discarges**.

|Facility Name|APR DRG Description|APR Severity of Illness Description|Discharges|Mean Charge|Median Charge|Mean Cost|
|----|----|----|----|----|----|----|
|Cayuga Medical Center at Ithaca|Viral Meningitis|Moderate|6|5738.0|5111.0|3949.0|
|Women And Children's Hospital Of Buffalo|Viral Meningitis|Moderate|31|6601.0|6182.0|2770.0|
|Millard Fillmore Suburban Hospital|Viral Meningitis|Moderate|6|6614.0|6784.0|2649.0|

<br>

# Data can be tricky   
1. Which illness has the most discharges?  It seems like an easy query, but data can be tricky.

Notice the "APR DRG Description" should be unique for each hospital, however, hospitals also have a label for how sever that illness is.  So each illness can be listed up to four times. They are separated and labeled accordingly with the "APR Severity of Illness Description".  This is annoying because it just is.
**To account for this you have to do a double group by...**  
*  Group the APR DRG Description with the of severity for each Illness.  
*  What is the most expensive type of illness?  

---

1. Find which hospital discharges the most cases of Viral Meningitis for all levels of severity.

| Facility Name | ... | Discharges |
| ------------- |-----|:----------:|
| North Shore University Hospital | ... | 158 |
| Montefiore Medical Center - Henry & Lucy Moses Div | ... | 152 |
| Strong Memorial Hospital | ... | 117 |

<br>


5. Find if there is a correlation between # of Discharges a hospital has and how much they charge. Hint use df.corr() *http://pandas.pydata.org/pandas-docs/stable/computation.html#correlation*

---

# Extra Credit:
Open ended question:  
1. Gain insights from data.  
2. Use Pandas Visualization tool (see [link](https://github.com/zipfian/graphing-basics) ) to plot insight  
3. Create heat map.  
### This is the end of the afternoon exercise.  If you have finished up early, find a data set you have always wanted to play with, and play with it.  
