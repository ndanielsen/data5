# GA-DC DAT5 Homework Week2
`echo "#GA-DC DAT5 Homework Week2" >> readme**.md`

######_With just enough illistrative code_

## CommandLine 
`echo "## CommandLine" >> rea*`

### Answers
`echo "### Answers" >> rea*`

####1. How many text messages are there? 
`echo "####1. How many text messages are there?" >> rea*`

> 5574 smsspamcollection.txt `wc -l smss* >> read*`

> The wc cli function with -l flag says that there are 5,574 lines in the smsspam collection

> With awk, 5574 lines in file `awk 'END { print NR }' sms*'`


####2. What is the average number of words per text? What is the average number of characters per text?

>  92479 smsspamcollection.txt `wc -w smss >> read*`

> 477907 smsspamcollection.txt `wc -c smss >> read*`
