print("Welcome to your Bayes Theorem Probability Calculator")

#Having user input known data into the equation by part
P1 = float(input("What is the probability of occurance given your input?: "))
P2 = float(input("What is the probability of no occruance given your input?: "))
P3 = float(input("What is the probability of occurance?: "))
P4 = float(input("What is the probability of no occurance?: "))

#Taking user data and solving for the unknown numerical value
P5 = round((P1*P3)+(P2*P4) ,2)

#Solving for probability in decimal form using Bayes Theorem
Answer = ((P1/P5) * P3)

#Printing answer in percentage form
print("The calculated probability to your question is:", round((Answer * 100, 2))
