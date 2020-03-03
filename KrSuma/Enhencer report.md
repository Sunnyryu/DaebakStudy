Jae Sun Lee
 
3/3/2020
Report on the key features on the target websites’ services:
“Auto Data Preparation”
-the ability to accept a wide variety of input files
-auto data cleaning and preparation 
“Predict likelihood of purchase”
-for both first-time buyers + returning customers
-choice of Machine Learning Algorithms to choose from
-compares all the result to obtain the best result
“Helps choose the right campaign”
-find customers based on offers and discount campaigns
Application goals (top-down priority):
1. Multidimensional analysis of sales, customers, products, time, region, etc.
2. Analysis of effectiveness of sales campaign
3. Product recommendation + cross reference
4. Customer retention
5. Design and construction of data warehouses based on the benefits of data mining
Research Topics:
1. Prediction / Classification analysis based on classification and regression models of machine learning
2. Cluster analysis
3. Auto data cleaning and preparation (either by script or from data warehousing)




Our target business’ model is mainly based on prediction analysis, the key branch in machine learning and data mining. All of their features are in applications from data science, so I think there is nothing innovative about their business model (they provide a service nothing out of ordinary outside the scope of data science). What I think is interesting and is the selling point of their service is the ‘Free’ feature - they allow one to have 20,000 requests per month, 10,000 rows of data entry / service, and for a single user.  This allows the user to try the service out for free with a small amount of data samples they have, and decide whether they want to continue pushing all their data and analyze them by paying a subscription fee. 
I believe this is a good move in a few ways:
1) They have fresh data to analyze in-house and is able to make changes to their services based on the demands of the clients/market (even when there are little to no regular customers)
2) They are able to train their machine learning models - since the trial is free, there is little risk to use this data and make changes to their algorithms. 
3) Since it is free to use, it allows the clients to have a trial run and help them decide whether they want to continue using their service risk-free.
I think offering a free service indefinitely like this ultimately does the company a favor in the long run.
        What I think it would be the challenge in recreating their business model is the following:
1. Automatic Data Preparation and Cleaning - it seems like they do this by having a data warehouse. 
a) It differs from a database in that it’s sole purpose is to analyze, report, and integrate transaction data from different sources. 
b) The nature of data warehousing makes analysis and reporting easier.
I do not believe that this is our priority in development in our early stages but it is definitely something to consider in the near future.
2. Comparing results from the output of many machine learning models and finding the best result. This is the difficult part, because not only we would need models pre-trained from the start, but will need to make tweaks on the learning algorithms on the fly and have multiple models learning on the clients data, then compare their output of the predictions and choose the best one. The critical factors here will be time, efficiency and accuracy.
