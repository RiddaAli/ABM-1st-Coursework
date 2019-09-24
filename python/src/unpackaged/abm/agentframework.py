#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:26:33 2019

@author: gyral
"""

import random 

class Agent():
    
    def __init__(self, environment, agents, y = None, x = None):
        
        """
        This is the constructor, which is a method that is called when an 
        object (Agent) is created from a class. Furthermore, it allows the
        class to initialize its attributes/properties (e.g. move, eat etc.).
        """
# =============================================================================
#         self._y = random.randint(0,300)
#         self._x = random.randint(0,300)
# =============================================================================
        self.environment = environment
        self.agents = agents
        self.store = 0
        
        if (x == None):
            self._x = random.randint(0,300)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,300)
        else:
            self._y = y
            
 
    def set_y(self, y):
        """ Setters: Making y private """
        self._y = y
        
    def set_x(self, x):
        """ Setters: Making x private """
        self._x = x
        
    
    def get_y(self):
        """ Getters: because y is private """
        return self._y
    
    def get_x(self):
        """ Getters: because x is private """
        return self._x
    

    def move(self):
        """ Moving agents randomly:
            - Problem: agents might be missing from the graph if they ended up
              wandering off the edge.
            - Solution: Torus - permit agents leaving the top of an area to
              come in at the bottom and leaving left come in on the right side.
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
            
    def eat(self): 
        """ 
        Using the if statement to determine whether agents should eat the
        environment or not. 
        If the environment is greater than 10 than subtract 10 units from the 
        environment and add it to the agent's store.
        """
        if self.environment[self.get_y()][self.get_x()] > 10:
            self.environment[self.get_y()][self.get_x()] -= 10
            self.store += 10
            
# =============================================================================
# # Extension from practical 6 (I/O)  
# # Displaing information about agents' location and stores      
# =============================================================================
# =============================================================================
#     def __str__(self):
#         print("x location: ", self.get_x())
#         print("y location: ", self.get_y())
#         print("store: ", self.store)
# 
# =============================================================================

# =============================================================================
#  Calculating the distance to each of the other agent and if they tend to be
# within the neighbourhood distance and it sets the its and its neighbours 
# stores equal to the average of their two stores
# =============================================================================
             
    def share_with_neighbours(self, neighbourhood):
        """ 
        Looping through the agents in self.agents.
        1) Calculating the distance between self and the current other agent.
        2) If the distance is less than or equal to neighbourhood then add 
           self.store and agent.store.
        3) Calculate the average by dividing the sum by 2. 
        4) Store this average into both the self.store and agent.store.
        """
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average = (self.store + agent.store)/2
                self.store = average
                agent.store = average
                #print("Sharing " + str(distance) + " " + str(average))
                
            
                
# Calculating how far the agents are by using Pythagoras
    def distance_between(self, other_agent):
            """
            Agent 1 = self.
            Agent 2 = other_agent.
            Calculating the distance between Agent 1 and Agent 2 by using 
            Pythagoras.
            """
            return (((self.get_x() - other_agent.get_x())**2) +
                ((self.get_y() - other_agent.get_y())**2))**0.5


