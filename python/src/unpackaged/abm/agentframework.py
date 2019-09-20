#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:26:33 2019

@author: gyral
"""

import random 

class Agent():
    # Environment is a list
    def __init__(self, environment, agents, y = None, x = None):
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
            
    # Setters: Making y and x are private
    def set_y(self, y):
        self._y = y
        
    def set_x(self, x):
        self._x = x
        
    # Getters: because y and x are private
    def get_y(self):
        return self._y
    
    def get_x(self):
        return self._x
    

    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
            
    def eat(self): 
        # can you make it eat what is left?
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
        #print("Neighbour: ", neighbourhood)
        
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
            Agent 1 = self
            Agent 2 = other_agent
            Calculating the distance between Agent 1 and Agent 2 by using Pythagoras
            """
            return (((self.get_x() - other_agent.get_x())**2) +
                ((self.get_y() - other_agent.get_y())**2))**0.5


