## Syntax

#### 

## Viewing the first 5 elements of the dataset

purchase.head()

## Viewing the dataset info - shows all columns with its name and the count of the attributes

purchase.info()

## Counts how many attributes are in the specified dataset column

purchase["name of the column"].value_counts()

## View the summaryof the numerical attributes of the dataset column

purchase.describe()

# View the histogram of the dataset using matplotlib.pyplot

purchase.hist(...)
matplotlib.pyplot.show()



