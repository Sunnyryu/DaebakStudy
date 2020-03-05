import codecs
from math import sqrt

'''
program based on the collaborative filtering research - 
equations and algorithms based on the notes.
'''

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
                  "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                  "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},
         "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                    "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}
         }


class recommender:
    def __init__(self, data, k=1, metric='pearson', n=5):
        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}
        self.metric = metric

        if type(data).__name__ == 'dict':
            self.data = data

        # function to convert product id number into product name
        def convertProductID2Name(self, id):
            if id in self.productid2name:
                return self.productid2name[id]
            else:
                return id

        # return n top ratings for user with id
        def userRatings(self, id, n):
            print("Ratings for " + self.userid2name[id])
            ratings = self.data[id]
            print(len(ratings))
            ratings = list(ratings.items())
            ratings = [(self.converProductID2name(k), v) for (k, v) in ratings]
            ratings.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
            ratings = ratings[:n]
            for rating in ratings:
                print("%s\t%i" % (rating[0], rating[1]))

        def pearsonCorrelation(self, rating1, rating2):
            numerator = 0
            x = 0
            y = 0
            x_sqrd = 0
            y_sqrd = 0
            count = 0
            for key in rating1:
                if key in rating2:
                    numerator += (rating1[key] * rating2[key])
                    x += rating1[key]
                    y += rating2[key]
                    x_sqrd += pow(rating1[key], 2)
                    y_sqrd += pow(rating2[key], 2)
                    count += 1
            if count == 0:
                return 0
            numerator = numerator - (x * y) / count
            denominator1 = pow((x_sqrd - (pow(x, 2)) / count), 1 / 2)
            denominator2 = pow((y_sqrd - (pow(y, 2)) / count), 1 / 2)
            return numerator / (denominator1 * denominator2)

        # creating a sorted list of users based on their distance to the username
        def computeNearestNeighbor(self, username):
            distances = []
            for instance in self.data:
                if instance != username:
                    distance = self.fn(self.data[username], self.data[instance])
            distances.append((instance, distance))
            # sort based on distance -- closest first
            distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
            return distances
