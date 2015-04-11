import time
import itertools

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import scipy



class BigBoat(object):

    def __init__(self, file, state_num, knn_num):

        self.df = pd.read_csv(file)
        self.state_num = state_num
        self.knn_num = knn_num


    def setUP(self):

        pass
        


    def clean(self):

        self.df = self.df.fillna("missing") #### Missing Values replaced with 0

        def f(x): #### Change embarked to numeric location

            if x == "S":
                return 1
            elif x == "C":
                return 2
            elif x == "Q":
                return 3
            else:
                return 0

        self.df["Embarked"] = self.df.Embarked.apply(f)

        self.df["Sex"] = self.df.Sex.map({'male':1, "female":2}) #### Replacing Gender to numeric

    

        def a(x):   ### Replacing Missing Ages
            if x == "missing":
                return 0
            else:
                return x

        self.df["Age"] = self.df.Age.apply(a)


        def ms(x): ### Married woman feature creation (if Mrs or Miss)
            y = x.split()
            if y[1] == "Mrs.":
                return 1
            else:
                return 0
            
            return y[1] 

        self.df["married_female"] = self.df.Name.apply(ms)

    @staticmethod
    def evaluate(X, y, state_num, knn_num):
        """
        Evaluates numberous iterations of train-test-split with numberous nearest neighbors

        Returns the highest average score with the corresponding nearest neighbor
        """
        results = {}
        for state in xrange(1, state_num): ### Number of train-test-split iterations to do
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=state)
            for num in xrange(1, knn_num): #number of nearest neighbors to try
                knn = KNeighborsClassifier(n_neighbors=num)
                knn.fit(X_train, y_train)
                y_pred = knn.predict(X_test)
                score = metrics.accuracy_score(y_test, y_pred)
                if num not in results:
                    results[num] = list()
                    results[num].append(score)
                               
                else:
                    results[num].append(score)
        
        report = [] 
        for key, value in results.iteritems(): #reviews all results and returns the greatest average score with n_neighbors num
            report.append((np.mean(value), key))

        return max(report)


    def combo_gen(self):
        """
        Generates every possible combination of numberic columns
        """
        dfnum = self.df._get_numeric_data()
        del dfnum['PassengerId']
        del dfnum['Survived']
        lst = []
        for col in dfnum.columns:
            lst.append(col)

        combo = []
            
        for i in xrange(1, len(lst)+1):
            
            for x in itertools.combinations(lst, i):
                combo.append(list(x) )
            
        return combo    

    def feature_combination(self, combo, state_num, knn_num):
        now = time.time()
        column_list = []
        count = 0
        for elem in combo:
            X = self.df[elem].values 
            y = self.df.Survived.values
            column_list.append((self.evaluate(X, y, state_num, knn_num), elem))
            count +=1
        
        return max(column_list), count, round(time.time() - now, 0)


    def test(self):
        print self.df.head(5)


    def main(self):

        self.setUP()
        self.clean()
        combo = self.combo_gen()
        return self.feature_combination(combo, self.state_num, self.knn_num)

if __name__ == '__main__':
    
    boat = BigBoat("train.csv", 2, 10)

    print boat.main()