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



class Glass(object):

    def __init__(self, file, trials, knn_num, max_features):
    	self.header_row = header_row=['Id','RI','Na','Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
        self.df = pd.read_csv(file, names=self.header_row)
        self.trials = trials
        self.knn_num = knn_num
        self.max_features = max_features

        self.y = "Type" ### Test values
        self.Id = "Id" ### Id Column


    def setUP(self):

        pass
    

    def test(self):
        print self.df.head(5)
    
    def clean(self):
    	pass


    def combo_gen(self):
        """
        Generates every possible combination of numberic columns
        """
        dfnum = self.df._get_numeric_data()
        del dfnum[self.y]
        del dfnum[self.Id]

        lst = []
        for col in dfnum.columns:
            lst.append(col)

        if len(lst) < self.max_features:
        	self.max_features = len(lst)
 
       	k = self.max_features

        combo = []
        for i in xrange(1, k+1):
            for x in itertools.combinations(lst, i):
                combo.append(list(x) )
            
        return combo 



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
            report.append((round((np.mean(value)), 4), key))

        return max(report)


    def feature_combination(self, combo):
        start = time.time()
        column_list = []
        
        for columns in combo:
            X = self.df[columns].values 
            y = self.df[self.y].values
            evaluation = self.evaluate(X, y)
            column_list.append((evaluation, columns))

        result = max(column_list)
        timer = round(time.time() - start, 0)

        return result, len(combo), timer



    def report(self):
        result, columns, timer = self.results
        knn_test, permutations = result
        percentage, knn_num = knn_test

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts)
        date = st.strftime('%Y-%m-%d')
        clock = st.strftime('%H:%M:%S')
        

        test_report = """ \
        
#Test on %r at %r

%r Random train-test-split trials \n
%r Maximum Features (columns)
%r Total Feature permutations \n
%r KNN neighbors evaluated (upper range)  
\n

**%r Average Correct Prediction** \n

%r KNN Nearest Neighbors Selected \n
Features Selected: %r \n
\n
_%r seconds_ \n


        """ % (date, clock, self.trials, self.max_features, columns, self.knn_num, percentage, knn_num, permutations, timer) 
        

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
    
    glass = Glass("glass.csv", 10, 5, 10)

    print glass.main()

