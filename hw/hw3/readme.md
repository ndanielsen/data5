hello
#GA-DC DAT5 Homework Three
`echo "#GA-DC DAT5 Homework3" >> readme**.md`
######_With just enough illistrative code_




####
		Part 1
		Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
		into a DataFrame.  Try looking at the "head" of the file in the command line
		to see how the file is delimited and how to load it.
		Note:  You do not need to turn in any command line code you may use.
		
_Answer is verbose but I'll print the head of ten_




####
		Part 2
		Get familiar with the data.  Answer the following questions:
		- What is the shape of the data?  How many rows and columns are there?
		- What variables are available?
		- What are the ranges for the values in each numeric column?
		- What is the average value for each column?  Does that differ significantly
		  from the median?
		


#####Numerical only header
   mpg  cylinders  displacement  horsepower  weight  acceleration  model_year  \
0   18          8           307         130    3504          12.0          70   
1   15          8           350         165    3693          11.5          70   
2   18          8           318         150    3436          11.0          70   
3   16          8           304         150    3433          12.0          70   
4   17          8           302         140    3449          10.5          70   

   origin  
0       1  
1       1  
2       1  
3       1  
4       1  


392


9


[["Column 'mpg':'Max: 46.6 , Min:9.0"], ["Column 'cylinders':'Max: 8 , Min:3"], ["Column 'displacement':'Max: 455.0 , Min:68.0"], ["Column 'horsepower':'Max: 230 , Min:46"], ["Column 'weight':'Max: 5140 , Min:1613"], ["Column 'acceleration':'Max: 24.8 , Min:8.0"], ["Column 'model_year':'Max: 82 , Min:70"], ["Column 'origin':'Max: 3 , Min:1"]]


[["Column 'mpg':'Average: 23.4459183673"], ["Column 'cylinders':'Average: 5.47193877551"], ["Column 'displacement':'Average: 194.411989796"], ["Column 'horsepower':'Average: 104.469387755"], ["Column 'weight':'Average: 2977.58418367"], ["Column 'acceleration':'Average: 15.5413265306"], ["Column 'model_year':'Average: 75.9795918367"], ["Column 'origin':'Average: 1.57653061224"]]


[["Column 'mpg':'Median: 22.75"], ["Column 'cylinders':'Median: 4.0"], ["Column 'displacement':'Median: 151.0"], ["Column 'horsepower':'Median: 93.5"], ["Column 'weight':'Median: 2803.5"], ["Column 'acceleration':'Median: 15.5"], ["Column 'model_year':'Median: 76.0"], ["Column 'origin':'Median: 1.0"]]


[["Column 'mpg':'Difference: -0.695918367347"], ["Column 'cylinders':'Difference: -1.47193877551"], ["Column 'displacement':'Difference: -43.4119897959"], ["Column 'horsepower':'Difference: -10.9693877551"], ["Column 'weight':'Difference: -174.084183673"], ["Column 'acceleration':'Difference: -0.0413265306122"], ["Column 'model_year':'Difference: 0.0204081632653"], ["Column 'origin':'Difference: -0.576530612245"]]




####
		Part 3
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




####
		Part 4
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
		
_It seems that MPG has a inverse linear relationship with cylinders, displacement, horsepower, and weight. In general, also a linear relationship with model_year._
None
<bound method VroomData.answers of <__main__.VroomData object at 0x7f6f30904e90>>
