#GA HW7 UCI Glass Identification

####_Iterative Results Using KNN Clustering_

[UCI Glass Identification Data Set](http://archive.ics.uci.edu/ml/datasets/Glass+Identification)<br>
Abstract: From USA Forensic Science Service; 6 types of glass; defined in terms of their oxide content (i.e. Na, Fe, K, etc)

###Data Description

No missing attributes

1. Id number: 1 to 214
2. RI: refractive index
3. Na: Sodium (unit measurement: weight percent in corresponding oxide, as 
              are attributes 4-10)
4. Mg: Magnesium
5. Al: Aluminum
6. Si: Silicon
7. K: Potassium
8. Ca: Calcium
9. Ba: Barium
10. Fe: Iron
11. Type: Type of glass


###Conclusion

Based upon the dataset and the below tests, I conclude that the best predictive ability using this small data set is 72.43 %. See last test.

         
#Test on '2015-04-12' at '09:28:40'

2 Random train-test-split trials 

511 Total feature permutations 

10 KNN neighbors evaluated (upper range)  



**0.7963 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_4.0 seconds_ 



                 
#Test on '2015-04-12' at '09:30:05'

2 Random train-test-split trials 

511 Total Feature permutations 

100 KNN neighbors evaluated (upper range)  



**0.7963 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_61.0 seconds_ 



                 
#Test on '2015-04-12' at '09:34:43'

10 Random train-test-split trials 

511 Total Feature permutations 

50 KNN neighbors evaluated (upper range)  



**0.7243 Average Correct Prediction** 


1 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba'] 



_234.0 seconds_ 


####Added Maximum Feature Parmeter 
##(example: only 3 numeric Features tests)
                 




                 
#Test on '2015-04-12' at '10:05:31'

5 Random train-test-split trials 

2 Maximum features (Features)
45 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7083 Average Correct Prediction** 


11 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Ba'] 



_2.0 seconds_ 



                 
#Test on '2015-04-12' at '10:05:49'

5 Random train-test-split trials 

3 Maximum features (Features)
129 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7361 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['Na', 'Al', 'Ca'] 



_6.0 seconds_ 



                 
#Test on '2015-04-12' at '10:06:10'

5 Random train-test-split trials 

4 Maximum features (Features)
255 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7454 Average Correct Prediction** 


1 KNN Nearest Neighbors Selected 

Features Selected: ['Mg', 'Al', 'K', 'Ca'] 



_12.0 seconds_ 



                 
#Test on '2015-04-12' at '10:06:39'

5 Random train-test-split trials 

5 Maximum features (Features)
381 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7546 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['Na', 'Mg', 'Al', 'K', 'Ca'] 



_20.0 seconds_ 



                 
#Test on '2015-04-12' at '10:07:28'

5 Random train-test-split trials 

6 Maximum features (Features)
465 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7593 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_22.0 seconds_ 



                 
#Test on '2015-04-12' at '10:08:07'

5 Random train-test-split trials 

7 Maximum features (Features)
501 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7593 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_24.0 seconds_ 



                 
#Test on '2015-04-12' at '10:08:53'

5 Random train-test-split trials 

8 Maximum features (Features)
510 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7593 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_27.0 seconds_ 



                 
#Test on '2015-04-12' at '10:09:36'

5 Random train-test-split trials 

9 Maximum features (Features)
511 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7593 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_25.0 seconds_ 



                 
#Test on '2015-04-12' at '10:11:17'

5 Random train-test-split trials 

9 Maximum features (Features)
511 Total Feature permutations 

15 KNN neighbors evaluated (upper range)  



**0.7593 Average Correct Prediction** 


5 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Fe'] 



_24.0 seconds_ 



                 
#Test on '2015-04-12' at '10:12:33'

10 Random train-test-split trials 

3 Maximum features (Features)
129 Total Feature permutations 

30 KNN neighbors evaluated (upper range)  



**0.6996 Average Correct Prediction** 


9 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Ba'] 



_31.0 seconds_ 



                 
#Test on '2015-04-12' at '10:13:50'

10 Random train-test-split trials 

4 Maximum features (Features)
255 Total Feature permutations 

30 KNN neighbors evaluated (upper range)  



**0.716 Average Correct Prediction** 


1 KNN Nearest Neighbors Selected 

Features Selected: ['Mg', 'Al', 'K', 'Ca'] 



_59.0 seconds_ 



                 
#Test on '2015-04-12' at '10:15:46'

10 Random train-test-split trials 

5 Maximum features (Features)
381 Total Feature permutations 

30 KNN neighbors evaluated (upper range)  



**0.716 Average Correct Prediction** 


1 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Mg', 'Al', 'K', 'Ca'] 



_90.0 seconds_ 



                 
#Test on '2015-04-12' at '10:22:35'

10 Random train-test-split trials 

9 Maximum features (Features)
511 Total Feature permutations 

30 KNN neighbors evaluated (upper range)  



**0.7243 Average Correct Prediction** 


1 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba'] 



_128.0 seconds_ 



                 
#Test on '2015-04-12' at '10:26:15'

10 Random train-test-split trials 

9 Maximum Features (columns)
511 Total Feature permutations 

5 KNN neighbors evaluated (upper range)  



**0.7243 Average Correct Prediction** 


1 KNN Nearest Neighbors Selected 

Features Selected: ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba'] 



_15.0 seconds_ 



        