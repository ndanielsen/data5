~~Hello World!~~
#GA-DC DAT5 Homework Four Visualizing Auto Data
######_With just enough illustrative code_
###Part 1




		Part 1
		Produce a plot that compares the mean mpg for the different numbers of cylinders.
		


![Image](cylinders_by_mean_mpg.png)



		self.df.groupby('cylinders').mpg.mean().plot(kind='bar')
		plt.title("Comparing Mean MPG for Different Numbers of Cylinders")
		plt.ylabel("MPG")
		plt.savefig('cylinders_by_mean_mpg.png', dpi=50)
		


_It seems clear that the most efficent number of cylinders is four and declines steeply after that._
###Part 2




		Part 2
		Use a scatter matrix to explore relationships between different numeric variables.
		


![Image](scatter_matrix.png)



		self.dfnum = self.df._get_numeric_data()
		pd.scatter_matrix(self.dfnum, alpha=0.2, diagonal='hist')
		
		plt.savefig('scatter_matrix.png', dpi=250)

		


_After looking at the entire scatter plot of numeric data, it seems that MPG is the most interesting variable to compare, so I'll make another scatterplot_
####Taking a closer look at MPG and how other average variables relate to it


![Image](histo_matrix_mpg.png)



		self.dfnum.groupby('mpg').mean().hist(alpha=0.5, bins=15)
		plt.savefig('histo_matrix_mpg.png', dpi=250)
		


_For acceleration, it seems clear that there is a sweet spot around 16.5 for best MPG 		For displacement, weight and horsepower it seems clear that as they increase, MPG goes down. 		For model year, it trends than over time the MPG gets better._
###Part 3




		Part 3
		Use a plot to answer the following questions:
		-Do heavier or lighter cars get better mpg?
		-How are horsepower and displacement related?
		-What does the distribution of acceleration look like?
		-How is mpg spread for cars with different numbers of cylinders?
		-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
		create a new column that encodes whether a year is before or after 1975.)
		


![Image](http://media.giphy.com/media/13HBDT4QSTpveU/giphy.gif)



		


_In progress_
