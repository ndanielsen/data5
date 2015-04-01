hello
#GA-DC DAT5 Homework Three
`echo "#GA-DC DAT5 Homework3" >> readme**.md`
######_With just enough illistrative code_




####Part 1
		Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
		into a DataFrame.  Try looking at the "head" of the file in the command line
		to see how the file is delimited and how to load it.
		Note:  You do not need to turn in any command line code you may use.
		
_Answer is verbose but I'll print the head of five_
   mpg  cylinders  displacement  horsepower  weight  acceleration  model_year  \
0   18          8           307         130    3504          12.0          70   
1   15          8           350         165    3693          11.5          70   
2   18          8           318         150    3436          11.0          70   
3   16          8           304         150    3433          12.0          70   
4   17          8           302         140    3449          10.5          70   

   origin                   car_name  
0       1  chevrolet chevelle malibu  
1       1          buick skylark 320  
2       1         plymouth satellite  
3       1              amc rebel sst  
4       1                ford torino  

[5 rows x 9 columns]




####Part 2
		Get familiar with the data.  Answer the following questions:
		- What is the shape of the data?  How many rows and columns are there?
		- What variables are available?
		- What are the ranges for the values in each numeric column?
		- What is the average value for each column?  Does that differ significantly
		  from the median?
		


#####Numerical values only with header of three
   mpg  cylinders  displacement  horsepower  weight  acceleration  model_year  \
0   18          8           307         130    3504          12.0          70   
1   15          8           350         165    3693          11.5          70   
2   18          8           318         150    3436          11.0          70   

   origin  
0       1  
1       1  
2       1  

[3 rows x 8 columns]


######Number of Rows
392


######Number of Columns
9
####acceleration's Calculations
{'Max': 24.800000000000001, 'Average': 15.541326530612228, 'Difference': -0.041326530612227685, 'Median': 15.5, 'Min': 8.0}
####mpg's Calculations
{'Max': 46.600000000000001, 'Average': 23.445918367346941, 'Difference': -0.69591836734694112, 'Median': 22.75, 'Min': 9.0}
####model_year's Calculations
{'Max': 82, 'Average': 75.979591836734699, 'Difference': 0.020408163265301482, 'Median': 76.0, 'Min': 70}
####cylinders's Calculations
{'Max': 8, 'Average': 5.4719387755102042, 'Difference': -1.4719387755102042, 'Median': 4.0, 'Min': 3}
####weight's Calculations
{'Max': 5140, 'Average': 2977.5841836734694, 'Difference': -174.0841836734694, 'Median': 2803.5, 'Min': 1613}
####displacement's Calculations
{'Max': 455.0, 'Average': 194.41198979591837, 'Difference': -43.411989795918373, 'Median': 151.0, 'Min': 68.0}
####horsepower's Calculations
{'Max': 230, 'Average': 104.46938775510205, 'Difference': -10.969387755102048, 'Median': 93.5, 'Min': 46}
####origin's Calculations
{'Max': 3, 'Average': 1.5765306122448979, 'Difference': -0.57653061224489788, 'Median': 1.0, 'Min': 1}




####Part 3
		Use the data to answer the following questions:
		- Which 5 cars get the best gas mileage?  
		- Which 5 cars with more than 4 cylinders get the best gas mileage?
		- Which 5 cars get the worst gas mileage?  
		- Which 5 cars with 4 or fewer cylinders get the worst gas mileage?
		


#####Best Five MPG
320               mazda glc
327     honda civic 1500 gl
323    vw rabbit c (diesel)
388               vw pickup
324      vw dasher (diesel)
Name: car_name, dtype: object


#####Four Cylcinders with Best Five MPG
381    oldsmobile cutlass ciera (diesel)
325                  audi 5000s (diesel)
330                        datsun 280-zx
355                         volvo diesel
304                   chevrolet citation
Name: car_name, dtype: object


#####Worst Five MPG
28             hi 1200d
26            chevy c20
25            ford f250
27           dodge d200
123    oldsmobile omega
Name: car_name, dtype: object


#####Four Cylcinders with Worst Five MPG
110          maxda rx3
75     volvo 145e (sw)
119        volvo 144ea
70     mazda rx2 coupe
111         ford pinto
Name: car_name, dtype: object




####Part 4
		Use groupby and aggregations to explore the relationships 
		between mpg and the other variables.  Which variables seem to have the greatest
		effect on mpg?
		Some examples of things you might want to look at are:
		- What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders,
		  4 cylinders, 5 cylinders, etc)?
		- Did mpg rise or fall over the years contained in this dataset?
		- What is the mpg for the group of lighter cars vs the group of heaver cars?
		Note: Be creative in the ways in which you divide up the data.  You are trying
		to create segments of the data using logical filters and comparing the mpg
		for each segment of the data.
		
self.df.groupby(['model_year', 'mpg']).mean().sort(ascending=True)
_It seems that MPG has a inverse linear relationship with cylinders, displacement, horsepower, and weight. In general, also a linear relationship with model_year._
None
