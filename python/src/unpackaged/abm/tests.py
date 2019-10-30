#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:55:52 2019

@author: gyral
"""

import agentframework
import csv
import pytest
import requests
import bs4

# =============================================================================
# # Creating an empty list called "environment" 
# (as it will store environmental data) to store the data read from the csv
# file into a 2D list  
# ============================================================================= 
environment = []

# Reading the data from the csv file "in.csv" for pixelation" 
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
#    Adding the values from each row to the "environment" list making it a 
#    2D List
# =============================================================================
     environment.append(rowlist)
     
# Once done with the reader close the file
f.close()


num_of_agents = 2

# =============================================================================
# Reading the data from the specified url, "read_site" return the response 200,
# which means successful execution of the request
# =============================================================================
read_site = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')


# Getting the content of the HTML page (including HTML tags) by using ".text"
content = read_site.text

# Using the "Beautiful Soup" Python library to pull data out of HTML
soup = bs4.BeautifulSoup(content, 'html.parser')


# =============================================================================
# # Using the attribute "class" in searches by putting it into a dictionary and
# then passing the dictionary into the "find_all()" as the "attrs" argument
# =============================================================================
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


# Creating the agents
agents = []
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    


def test_move():
    """ 
    Testing the "move()" function by specifying the position of the first 
    agent (initially at position (0,0)),making the agent move and then ensuring
    that its x and y values are within the correct range (0,299).
    """
    agents[0].set_y(0)  
    agents[0].set_x(0)

    agents[0].move()

    assert agents[0].get_y() >= 0 and agents[0].get_y() < 300
    assert agents[0].get_x() >= 0 and agents[0].get_x() < 300
    
    
    
def test_eat():
    """ 
    Testing the "eat()" function by making the second agent eat 30 times, 
    then getting its x and y values and ensuring that the environment is not
    empty. 
    """
    for _ in range(30):
        agents[1].eat()
    x = agents[1].get_x()
    y = agents[1].get_y()
    
    # Ensuring that the environment is never empty   
    assert environment[y][x] > 0
    
    
    
def test_distance_between():
    """ 
    Testing the  "distance_between()" function by adding two agents to the 
    "agents_list" and then ensuring that there is a distance between the first
    and second agent, whereas there is no distance between the second agent and 
    itself. 
    """
    environment = [[2, 2],[ 2, 2]]
    
    agents_list = []
    agents_list.append(agentframework.Agent(environment,agents_list,0, 0))
    agents_list.append(agentframework.Agent(environment,agents_list, 0, 1))
    
    assert agents_list[0].distance_between(agents_list[1]) == 1, "There is a distance!"
    assert agents_list[1].distance_between(agents_list[1]) == 0, "There is no distance!"
    
    
    
def test_share():
    """ 
    Testing the "share_with_neighbours()" function by creating 2 agents:
    first agent at position(5,5) and the second agent at position (4,4). 
    Then, making the first agent eat. Printing the storage of the 2 agents 
    before sharing. Making them share within the neighbourhood (radius) 4. 
    Lastly, testing that the storage of the 2 agents is the same.
    """
    first_agent = agents[0]
    second_agent = agents[1]
    
    first_agent.set_x(5)
    first_agent.set_y(5)
    
    second_agent.set_x(4)
    second_agent.set_y(4)
    
    first_agent.eat()
    
    print('Before sharing the storage of the agents are ', first_agent.store,
          second_agent.store)
    
    first_agent.share_with_neighbours(4)
    
    print('After sharing the storage of the agents are ', first_agent.store, 
          second_agent.store)
    
    assert first_agent.store == second_agent.store
   
    
pytest.main()

# =============================================================================
# As it is evident from the comments below (copied and pasted from the console),
# all the tests have successfully PASSED:
# =============================================================================
# =============================================================================
# (base) Riddas-MacBook-Pro:abm riddaali$ python -m pytest -v tests.py
# ============================================ test session starts ============
# platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- //anaconda3/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/riddaali/Documents/GitHub/ABM-1st-Coursework/python/src/unpackaged/abm
# plugins: openfiles-0.3.2, arraydiff-0.3, doctestplus-0.3.0, remotedata-0.3.1
# collected 4 items                                                                                           
# 
# tests.py::test_move PASSED                                            [ 25%]
# tests.py::test_eat PASSED                                             [ 50%]
# tests.py::test_distance_between PASSED                                [ 75%]
# tests.py::test_share PASSED                                           [100%]
# =============================================================================
