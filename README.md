Mapper and Reducer programs are coded to partition the data given in text file into 5 classes as follows: 
class 1 contains transactions s.t. the item count is between 1-10, class2 for 11-20, and so on till class5 having 41-50 item count; and computes the total amount obtained for each class. 

input:  
1: 100 200 400 500
2: 10 50 5 25 89 20 35 91 78 82 150 125
3: 100 300
Here tx 1 and tx 3 belong to class 1 as the item count for each is between 1 - 10, while tx 2 belongs to class 2. The total amount from the sales for class 1 is the sum of the costs of all the items from tx 1 and tx 3. 

e.g. output 
class1, 1600  
class2, 760
