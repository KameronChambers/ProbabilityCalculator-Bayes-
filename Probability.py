print("Welcome to your Bayes Probability Calculator")
print("Insert answers as decimals instead of whole numbers: (eg; 99% -> 0.99)\n")

#Gathering user input for equations
pb_given_a = float(input("What is the probability of B given A? Pr(B|A): "))
pb_notgiven_a = float(input("What is the probability of B not given A? Pr(B|notA): "))
p_a = float(input("What is the probability of A? Pr(A): "))

#Automatically compute complement of A
pnot_a = 1.0 - p_a

#Calculating missing numerical value (p_b) Pr(B)
#The total probability of B occuring at all
p_b = (pb_given_a * p_a) + (pb_notgiven_a * pnot_a)

# Guard against division by zero
if p_b == 0:
    print("\nError: Pr(B) evaluates to 0. Pr(A|B) is undefined.")
else:
    # Bayes' Theorem: Pr(A|B) = (Pr(B|A) * Pr(A)) / Pr(B)
    posterior = (pb_given_a * p_a) / p_b
    percentage = round(posterior * 100, 2)
    print(f"\nThe calculated probability Pr(A|B) is: {percentage}%")
