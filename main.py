# Programmer: Gryphen Clark
# Date: Sept 13th 2021
# Description: input a code for pizza slices

num_people = int(input("How many people are there? "))
num_pizzas = int(input("How many pizzas are there? "))
num_slices_pizza = int(input("How many slices per pizza are there? "))
cost_pizza = float(input("How much does the pizza's cost? "))

#calculating total slices by each pizza and how many slices there are
total_slices = num_pizzas * num_slices_pizza
slices_person = total_slices / num_people
cost_total = num_pizzas * cost_pizza
# print statements
print(f"there are {slices_person:.2f} slices per person.")
print(f"the cost of the pizza's are ${cost_total:.2f}.")