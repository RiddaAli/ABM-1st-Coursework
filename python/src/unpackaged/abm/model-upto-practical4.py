# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:04:46 2019

@author: gyral
"""
# Importing the "random" library
import random

# Importing the "operator" library
import operator 

# Importing the "pyplot" from the "matplotlib" library
import matplotlib.pyplot 
# Importing the time library to check how long a section of code takes to run in seconds
import time

start = time.clock()
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

# Creating a new variable "num_of_agents" setting it equal to 10
num_of_agents = 10

num_of_iterations = 100

# initialise a list of agents
agents = []

# Making 10 agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


# Moving agents randomly:
    # Torus - permit agents leaving the top of an area to come in at the bottom
    # and leaving left come in on the right side
 
# Using a for loop to repeat the iteration 100 times    
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

    

# Using the matplot librabry to plot our agents           
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

distances = []
# Using nested loops to go through the agents e.g(agent a and agent b) - comparing from and to
for i in range(num_of_agents):
    for j in range(i+1,num_of_agents):
        distance = distance_between(agents[i], agents[j])
        distances.append(distance)
        print(i, j, distance)
        
end = time.clock()

print("time = " + str(end - start))

# Calculating the maximum and minimum distances between agents
max_distance = max(distances)
min_distance = min(distances)
# =============================================================================
# # randomly moving agent 0
# y0 = agents[0][0]
# x0 = agents[0][1]
# 
# random_number_y = random.random()
# 
# =============================================================================
# =============================================================================
# # A 50% chance of moving agents
# if random_number_y < 0.5:
#     y0 = y0 + 1
# else:
#     y0 = y0 - 1
#     
# random_number_x = random.random()
# 
# if random_number_x < 0.5:
#     x0 = x0 + 1
# else:
#     x0 = x0 - 1
# 
# print(y0, x0)
# 
# 
# # randomly moving agent 1
# y1 = agents[1][0]
# x1 = agents[1][1]
# random_number_y1 = random.random()
# 
# 
# if random_number_y1 < 0.5:
#     y1 = y1 + 1
# else:
#     y1 = y1 - 1
#     
# random_number_x1 = random.random()
# 
# if random_number_x1 < 0.5:
#     x1 = x1 + 1
# else:
#     x1 = x1 - 1
# 
# print(y1, x1)
# =============================================================================

# =============================================================================
# # A 50% chance of moving agents up or down
# if random.random() < 0.5:
#     agents[0][0] += 1
# else:
#     agents[0][0] -= 1
# 
# if random.random() < 0.5:
#     agents[0][1] += 1
# else:
#     agents[0][1] -= 1
# 
# if random.random() < 0.5:
#     agents[0][0] += 1
# else:
#     agents[0][0] -= 1
# 
# if random.random() < 0.5:
#     agents[0][1] += 1
# else:
#     agents[0][1] -= 1
# 
# =============================================================================

# =============================================================================
# # Calculating how far the agents are by using Pythagoras
# result = (((y0-y1)**2) + ((x0-x1)**2))**0.5
# print(result)
# 
# =============================================================================

# =============================================================================
# # Finding out which agent is furthest north (larger y value)
# print(max(agents))
# =============================================================================


# =============================================================================
# # Using the matplot librabry to plot our agents
# matplotlib.pyplot.ylim(0, 100)
# matplotlib.pyplot.xlim(0, 100)
# matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
# matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
# # =============================================================================
# # # Finding out which agent is furthest east (larger x value)
# # m = max(agents, key=operator.itemgetter(1))
# # matplotlib.pyplot.scatter(m[1],m[0], color='red')
# # =============================================================================
# matplotlib.pyplot.show()
# 
# =============================================================================
# =============================================================================
# Problem: agents might be missing from the graph if they ended up wandering off the edge
# Solution: Torus - permit agents leaving the top of an area to come in at the bottom and leaving left come in on the right side
# =============================================================================
