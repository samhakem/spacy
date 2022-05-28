# Exploring the model

Let’s see how the model performs on unseen data! To speed things up a little, we already ran a trained pipeline for
the label "GADGET" over some text. Here are some of the results:


Text	Entities
Apple is slowing down the iPhone 8 and iPhone X - how to stop it	(iPhone 8, iPhone X)
I finally understand what the iPhone X ‘notch’ is for	(iPhone X,)
Everything you need to know about the Samsung Galaxy S9	(Samsung Galaxy,)
Looking to compare iPad models? Here’s how the 2018 lineup stacks up	(iPad,)
The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple	(iPhone 8, iPhone 8)
what is the cheapest ipad, especially ipad pro???	(ipad, ipad)
Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics	(
Samsung Galaxy,)
Out of all the entities in the texts, how many did the model get correct? Keep in mind that incomplete entity spans
count as mistakes, too! Tip: Count the number of entities that the model should have predicted. Then count the
number of entities it actually predicted correctly and divide it by the number of total correct entities.

70% On our test data, the model achieved an accuracy of 70%.
