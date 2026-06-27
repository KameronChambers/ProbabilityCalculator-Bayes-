# ProbabilityCalculator-Bayes-
Interactive calculator for updating the probability of a hypothesis as more evidence becomes available using Bayes Theorem.

How it Works:
The calculator users Bayes Theorem to solve for posterior probability: Pr(A|B) 
Equation: Pr(A|B) = (Pr(B|A) * Pr(A)) / Pr(B)

Getting Started / Usage:
1. Clone the repository to your local machine or open it in a GitHub Codespace.
2. Open your terminal or command prompt in the project directory.
3. Execute the script by typing: python Probability.py

Warnings:
*Data must be inputed as decimal values between 0.0 and 1.0

A. Sample Test Run: 
B. Scenario: A high-tech factory uses an automated scanner to detect defective computer chips on an assembly line. If a chip is defective, the scanner correctly flags it as defective 98% of the time. If the chip is not defective, the scanner correctly clear is (labels it as non-defective) only 95% of the time. Statistically, only 2% of all chips produced on this assembly line are actually defective.

C. Question: If a randomly chosen chip is flagged by the scanner as defective, what is the probability that the chip is actually defective?

D. Data To Input:
What is the probability of B given A? Pr(B|A): 0.98
What is the probability of B not given A? Pr(B|notA): 0.05
What is the probability of A? Pr(A): 0.02
What is the probability of notA? Pr(notA): 0.98

E. Answer:
The calculated probability of Pr(A|B) is: 28.57 
