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

