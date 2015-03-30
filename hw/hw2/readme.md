# GA-DC DAT5 Homework Two
`echo "#GA-DC DAT5 Homework2" >> readme**.md`

######_With just enough illistrative code_

## CommandLine 
`echo "## CommandLine" >> rea*`

### Answers
`echo "### Answers" >> rea*`

####1. How many text messages are there? 
`echo "####1. How many text messages are there?" >> rea*`

5574 smsspamcollection.txt `wc -l smss* >> read*`

_The wc cli function with -l flag says that there are 5,574 lines in the smsspam collection_

With awk, 5574 lines in file `awk 'END { print NR }' sms*'`


####2. What is the average number of words per text? What is the average number of characters per text?

92479 smsspamcollection.txt `wc -w smss* >> read*`

5574 smsspamcollection.txt `wc -l smss* >> read*`

_Average number of words per text is 92479 / 5574 = 16.59_

477907 smsspamcollection.txt `wc -c smss* >> read*`

_Average number of characters per text is 477907 / 5574 = 85.74_


####3.How many messages are spam? How many are ham?

_With awk `awk "/^ham/ { print $1 }" sms* | wc -l` is 4827 && `awk "/^spam/ { print $1 }" sms* | wc -l` is 747_



####4. Is there a difference between the number of words per text and characters per text in messages that are spam vs. those that are ham? What are these numbers?

#####Ham

73870 ham_messages.txt `wc -w ham*`

369499 ham_messages.txt `wc -c ham*`

4827 ham_messages.txt `wc -l ham*`

_Average number of words per ham text is 73870 / 4827 = 15.30_

_Average characters per ham text is 3694499 / 4827 =  76.55_


#####Spam

18609 spam__messages.txt `wc -w spam*`

108408 spam__messages.txt `wc -c spam*`

747 spam__messages.txt `wc -l spam*`

_Average number of words per spam text is 18609 / 747 = 24.91_

_Average characters per ham spam is 108408 / 747 =  145.12_

__Conclusion: Spam sms generally are longer and have more words than ham__

####5. Separate the spam and ham messages into files "spam\_messages.txt" and ham\_messages.txt.

> With awk `awk "/^ham/ { print $1 }" sms* > ham_messages.txt` && `awk "/^spam/ { print $1 }" sms* > spam__messages.txt`

> With cli `grep "spam" sms* > spam_messages.txt` && ``grep "ham" sms* > ham_messages.txt`


