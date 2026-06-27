print("Welcome to your Byers Probability Calculator")
print("Insert answers as decimals instead of whole numbers: (eg; 99% -> 0.99)")

#Gathering user input for equations
pb_given_a = float(input("What is the probability of B given A? Pr(B|A): "))
pb_notgiven_a = float(input("What is the probability of B not given A? Pr(B|notA): "))
p_a = float(input("What is the probability of A? Pr(A): "))
pnot_a = float(input("What is the probability of notA? Pr(notA): "))

#Calculating missing numerical value (p_b) Pr(B)
#The total probability of B occuring at all
p_b = (pb_given_a * p_a) + (pb_notgiven_a * pnot_a)

#Calculating the final answer using Byers Theorem
# Pr(A|B) = (Pr(B|A) * Pr(A)) / Pr(B)
Answer = (pb_given_a*p_a)/p_b

#Turning answer into a percentage
Percentage = round(Answer*100, 2)

#Print results as a percentage
print("The calculated probability of Pr(A|B) is:", Percentage, "%")
