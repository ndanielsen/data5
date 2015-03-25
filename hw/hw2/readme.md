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


####3.How many messages are spam? How many are ham?

> With awk `awk "/^ham/ { print $1 }" sms* | wc -l` is 4827 && `awk "/^spam/ { print $1 }" sms* | wc -l` is 747



####4. Is there a difference between the number of words per text and characters per text in messages that are spam vs. those that are ham? What are these numbers?

> Something

####5. Separate the spam and ham messages into files "spam\_messages.txt" and ham\_messages.txt.

> With awk `awk "/^ham/ { print $1 }" sms* > ham_messages.txt` && `awk "/^spam/ { print $1 }" sms* > spam__messages.txt`

> With cli `grep "spam" sms* > spam_messages.txt` && ``grep "ham" sms* > ham_messages.txt`


