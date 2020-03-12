## Item Based Filtering

Explcit Ratings: users explicitly rates the item.

Implicit Ratings: user does not rate; but rather, we observe their behaviour.

ex) tracking what users click online on the webpage

We use this to post stuffs like "Frequently bought together", etc...

ex) song is played 50 times, user likes this song, etc.

#### Problem with explicit ratings:
1. people are lazy
2. people can lie or give partial info
3. people don't update ratings

Implicit data solves this problem by simply observing the user's action and coming up with conclusion.

ex) clicks, time, repeated visits, referrals, etc.

-User based filtering needs a stored ratings from users to make recommendations. This can be a problem because 
to come up with a recommendation with huge dataset (~1 million for example) is a huge computational task.

-Item based filtering is simply using the model we built with the existing dataset to come up with a recommendation.

#### item-based collaborative filtering recommendation system:

-To compute the similarity between the items.

-we subtract the user's average rage ratings from each rating to compensation for grade inflation.

<a href="https://www.codecogs.com/eqnedit.php?latex=c(i,j)=\frac{\sum_{u\in{U}}(R_{u,i}-\bar{R}_{u})(R_{i,j}-\bar{R}_{u})}{\sqrt{\sum_{u\in{u}}(R_{u,i}-\bar{R}_{u})^{2}}\sqrt{\sum_{u\in{U}}(R_{u,j}-\bar{R}_{u})^{2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c(i,j)=\frac{\sum_{u\in{U}}(R_{u,i}-\bar{R}_{u})(R_{i,j}-\bar{R}_{u})}{\sqrt{\sum_{u\in{u}}(R_{u,i}-\bar{R}_{u})^{2}}\sqrt{\sum_{u\in{U}}(R_{u,j}-\bar{R}_{u})^{2}}}" title="c(i,j)=\frac{\sum_{u\in{U}}(R_{u,i}-\bar{R}_{u})(R_{i,j}-\bar{R}_{u})}{\sqrt{\sum_{u\in{u}}(R_{u,i}-\bar{R}_{u})^{2}}\sqrt{\sum_{u\in{U}}(R_{u,j}-\bar{R}_{u})^{2}}}" /></a>

where:

<a href="https://www.codecogs.com/eqnedit.php?latex=(R_{u,i}-\bar{R}_{u})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(R_{u,i}-\bar{R}_{u})" title="(R_{u,i}-\bar{R}_{u})" /></a>

is the rating R of item i from user u, minus the average (mean) rating for all the item the user rated.

-To make a prediction that user u will give item i using the similarity between the items:

<a href="https://www.codecogs.com/eqnedit.php?latex=p(u,&space;i)=\frac{\sum_{N\in{similarTo(i)}}(S_{i,N}&space;\times&space;R_{u,N})}{\sum_{N\in{similarTo(i)}}(|S_{i,N}|)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p(u,&space;i)=\frac{\sum_{N\in{similarTo(i)}}(S_{i,N}&space;\times&space;R_{u,N})}{\sum_{N\in{similarTo(i)}}(|S_{i,N}|)}" title="p(u, i)=\frac{\sum_{N\in{similarTo(i)}}(S_{i,N} \times R_{u,N})}{\sum_{N\in{similarTo(i)}}(|S_{i,N}|)}" /></a>

where:

p(u,i) is the prediction that user u will give the item i

N - each of items that user u rated that are similar to item i

S(i,j) - is the function S(i,j) 

R(u,N) - rating user u gave item N

#### Slope-one predictors collaborative filtering

-Easy to implement due to simplicity.

1. first, ahead of time (batch mode) we will compute all the deviation between 
every pair of items. 
2. then in the second phase, we make the predictions using the table of deviations.

-The average deviation of an item i with respect to j is:

(INSERT HERE)

where

(INSERT HERE)

is how many elements are in S and X is the entire set of all ratings 
(Card stands for cardinality).

-Then the Weighted slope-one calculation is as follows:

where

