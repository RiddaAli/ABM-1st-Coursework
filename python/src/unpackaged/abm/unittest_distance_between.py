#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:13:19 2019

@author: gyral
"""

import unittest
import agentframework

class TestDocs(unittest.TestCase):

    def test_distance_between(self):
        
        
        """ 
        Testing the  "distance_between()" function by adding two agents to the 
        "agents_list" and then testing that there is a distance between the 
        first and second agent, whereas there is no distance between the second
        agent and itself. 
        """
        environment = [[2, 2],[ 2, 2]]
        
        agents_list = []
        agents_list.append(agentframework.Agent(environment,agents_list,0, 0))
        agents_list.append(agentframework.Agent(environment,agents_list, 0, 1))
        
        assert agents_list[0].distance_between(agents_list[1]) == 1, "There is a distance!"
        assert agents_list[1].distance_between(agents_list[1]) == 0, "There is no distance!"
        
# =============================================================================
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# 
# OK
# =============================================================================


if __name__ == '__main__':
    unittest.main()
    

