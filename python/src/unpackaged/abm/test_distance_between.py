#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:13:19 2019

@author: gyral
"""

import pytest
import agentframework



def testing_distance_between():
    environment = [[2, 2],[ 2, 2]]
    
    agents_list = []
    agents_list.append(agentframework.Agent(environment,agents_list,0, 0))
    agents_list.append(agentframework.Agent(environment,agents_list, 0, 1))
    
    assert agents_list[0].distance_between(agents_list[1]) == 1, "There is a distance!"
    assert agents_list[1].distance_between(agents_list[1]) == 0, "There is no distance!"


pytest.main()
testing_distance_between()
