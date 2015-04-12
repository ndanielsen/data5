import time
import itertools
import datetime



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import scipy



class BigBoat(object):

    def __init__(self, file, trials, knn_num):

        self.df = pd.read_csv(file)
        self.trials = trials
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

        self.df["Married_Female"] = self.df.Name.apply(ms)


        def ag(x):
            if x == "missing":
                return 0
            else:
                return 1
            
        self.df['Age_Known'] = self.df.Age.apply(ag)

        self.df['Cabin_Known'] = self.df.Cabin.apply(ag)

        def l(x):
            for elem in x:
                try:
                    if int(elem):
                        return 0
                except ValueError:
                    return 1

        self.df["TicketswLetters"] = self.df.Ticket.apply(l)



    def evaluate(self, X, y):
        """
        Evaluates numberous iterations of train-test-split with numberous nearest neighbors

        Returns the highest average score with the corresponding nearest neighbor
        """
        results = {}
        for state in xrange(1, self.trials): ### Number of train-test-split iterations to do
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=state)
            for num in xrange(1, self.knn_num): #number of nearest neighbors to try
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
            report.append(((round(np.mean(value), 4)), key))

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

    def feature_combination(self, combo):
        start = time.time()
        column_list = []
        
        for columns in combo:
            X = self.df[columns].values 
            y = self.df.Survived.values
            column_list.append((self.evaluate(X, y), columns))
            


        result = max(column_list)
        timer = round(time.time() - start, 0)

        return result, len(combo), timer


    def test(self):
        print self.df.head(5)

    def report(self):
        result, count, timer = self.results
        knn_test, permutations = result
        percentage, knn_num = knn_test

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts)
        date = st.strftime('%Y-%m-%d')
        clock = st.strftime('%H:%M:%S')

        test_report = """ \
        
_Test on %r at %r_

%r Random train-test-split trials
%r Total column permutations 
c

*%r Average Correct Prediction*

%r KNN Nearest Neighbors Selected 
Columns Selected: %r

%r seconds


        """ % (date, clock, self.trials, permutations, self.knn_num, percentage, knn_num, columns, timer) 
        

        with open("readme.md", "a") as myfile:
            myfile.write(test_report)


    def main(self):

        self.setUP()
        self.clean()
        combo = self.combo_gen()
        self.results = self.feature_combination(combo)
        self.report()
        return self.results


if __name__ == '__main__':
    
    boat = BigBoat("train.csv", 5, 50)

    print boat.main()