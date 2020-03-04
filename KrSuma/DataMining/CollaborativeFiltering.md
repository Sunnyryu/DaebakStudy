Collaborative Filtering

This method makes recommendations based on the ratings of other people - people collaborate to come up with recommendations. 

Let x be rating A and y be rating B.

1) Manhattan Distance:

The easiest distance measure between the ratings of 2 elements on a plane.

Fast to compute, especially when there are millions of pairs of users to compare from.

<a href="https://www.codecogs.com/eqnedit.php?latex=|x_{1}&space;-&space;x_{2}|&plus;|y_{1}-y_{2}|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|x_{1}&space;-&space;x_{2}|&plus;|y_{1}-y_{2}|" title="|x_{1} - x_{2}|+|y_{1}-y_{2}|" /></a>


We can use the Minkowski Distance Metric to generalize the Manhattan Distance and Euclidean Distance:

<a href="https://www.codecogs.com/eqnedit.php?latex=d(x,y)&space;=&space;(\sum_{k=1}^{n}|x_{k}-y_{k}|^{r})^{1/r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d(x,y)&space;=&space;(\sum_{k=1}^{n}|x_{k}-y_{k}|^{r})^{1/r}" title="d(x,y) = (\sum_{k=1}^{n}|x_{k}-y_{k}|^{r})^{1/r}" /></a>

where

r=1: The formula is Manhattan Distance,
r=2: The formula is Euclidean Distance,
r=infinity: Supremum Distance.

2) Pearson Correlation Coefficient:

Say for example there is a table that compares the ratings of items from users.

Users will have different behaviors when it comes to rating items. For example, a user A seems to avoid rating in extremes. A's ratings range from 2 to 4, while user B seems to like everything and rates all items from 4 to 5. Some users might not even care and rate everything to 4.

In order to compare between two users, we need to measure the correlation between the ratings between them - that is, we need to know if user A's rating of '4' mean the same as user B's rating of '4's or '5's.

The Pearson Correlation Coefficient is a measure of correlation between two variables (in our case, the ratings of two users), the output ranging from -1 and 1 inclusive ([-1,1]).

1 will indicate perfect agreement, while -1 indicates perfect disagreement.

<a href="https://www.codecogs.com/eqnedit.php?latex=r=\frac{\sum_{i=1}^{n}(x_{i}-\bar{x})(y_{i}-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\bar{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\bar{y})^{2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r=\frac{\sum_{i=1}^{n}(x_{i}-\bar{x})(y_{i}-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\bar{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\bar{y})^{2}}}" title="r=\frac{\sum_{i=1}^{n}(x_{i}-\bar{x})(y_{i}-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\bar{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\bar{y})^{2}}}" /></a>

where 

n is sample size
xi and yi are the individual sample points with index i
x bar is the sample mean for x, likewise for y bar being the sample mean for y.