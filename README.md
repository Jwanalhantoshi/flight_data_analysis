# Flight Data Analysis

This project analyzes U.S. domestic flight data from 2013 using Python.

## Project Goals
- Analyze flight delays  
- Understand airline performance  
- Identify factors affecting arrival and departure times  

## Tools Used
- Python  
- Pandas  
- Seaborn  
- Matplotlib  

## Conclusion
The analysis revealed patterns in flight delays based on airline performance and departure times.  
Some airlines showed better efficiency, while others had higher delay rates.  

## Key Insights
- Evening flights had more delays  
- Some airlines performed better than others  
- Distance had limited impact on delays

##Function dictionary
pd.read_csv(): Loads the dataset from a CSV file into a DataFrame
df.head(): Displays the first rows of the dataset
df.shape: Returns the number of rows and columns
df.columns: Shows all column names in the dataset
df.info(): Provides general information about data types and non-null values
df.isnull().sum(): Counts missing values in each column
fillna(): Replaces missing values with a specified value
dropna(): Removes rows with missing values
mean(): Calculates the average of values
max(): Finds the maximum value
min(): Finds the minimum value
groupby(): Groups data based on a column
agg(): Applies multiple aggregation functions
count(): Counts the number of values
plot(): Creates general plots (line, bar, etc.)
plt.figure(): Sets the figure size
plt.title(): Adds a title to the plot
plt.xlabel(): Labels the x-axis
plt.ylabel(): Labels the y-axis
plt.grid(): Adds grid lines to the plot
plt.savefig(): Saves the plot as an image
plt.show(): Displays the plot

