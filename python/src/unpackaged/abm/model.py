import random
#import operator
import matplotlib.pyplot
import agentframework
import csv


# =============================================================================
# # How many agents? Number of agents is stored is inside the 
# "num_of_agents" variable
# =============================================================================
num_of_agents = 10

# =============================================================================
# # How many times we want to iterate? Number of iterations is stored inside 
# "num_of_iterations" variable
# =============================================================================
num_of_iterations = 100

# 20 is the radius around agents
neighbourhood = 20

# =============================================================================
# # Creating an empty list called "environment" 
# (as it will store environmental data) to move the data read from the csv
# file into a 2D list  
# =============================================================================
environment = []
# Reading the csv file called "in.csv" 
f = open('in.csv', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
 # A list of rows
for row in reader:
    # Creating an empty list called "rowlist" to store all the values
     rowlist = []
     
     # A list of value
     for value in row:
         rowlist.append(value)
# =============================================================================
#    # Adding the values from each row to the "environment" list making it a 
#    #2D List
# =============================================================================
     environment.append(rowlist)
     
# Once done with the reader close the file
f.close()

# Creating an empty list to store the agents
agents = []

# Creating the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


# Moving the agents
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
#agents[2].__str__()

# Using the matplot librabry to plot our agents        
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(300, 0)
# Checking that the data has beencread correctly by plotting it
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y())
matplotlib.pyplot.show()

# =============================================================================
# # Using nested for loops to go through the list of agents and then calling 
# the "distance_between()" function to calculate the distance between them
# =============================================================================
for agent1 in agents:
    for agent2 in agents:
        distance = agent1.distance_between(agent2)


