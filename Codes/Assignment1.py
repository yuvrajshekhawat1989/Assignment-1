from numpy import random

#Calculating the Probability experimentally

count = 0
i = 0
trials = 1000000
#array which stores the coins and their value with 100 50paise coins,50 Rs1 coins,20 Rs 2 coins, 10 Rs 5 coins 
arr = [0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,
0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,
0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,
0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,
0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,
5,5,5,5,5]

#PART A
while i < trials:
  x = random.choice(arr)

  if (x==0.50):
    count +=1

  i +=1    
#Experimental probability of picking 50p coins
experimental_prob_50p = count/trials

#Calculating Theoritical Probability
theoritical_prob_50p = (100/180)      #Since, There are 100 Rs 50p coins out of total 180 coins

#printing probabilities
print("The Theoretical Proability is: ",theoritical_prob_50p)
print("The Experimental Probability is: ",experimental_prob_50p)

#PART B
count = 0
i = 0
while i < trials:
  x = random.choice(arr)

  if (x!=5):
    count +=1

  i +=1    
#Experimental probability of picking 50p coins
experimental_prob_5 = count/trials

#Calculating Theoritical Probability
theoritical_prob_5 = (170/180)          #Since, There are 170 coins out of total 180 coins which are not Rs5 coins
#printing probabilities
print("The Theoretical Proability is: ",theoritical_prob_5)
print("The Experimental Probability is: ",experimental_prob_5)
