# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:01:36 2022


This file will store all of the functions
needed to parse the IRC chat file. 


@author: ls458663
"""

#%% imports 
import re


#%% function to get hours and minutes

def get_hours_minutes(row):
    pass



#%% test hours and minutes

log_open_row = '--- Log opened Tue Sep 20 00:01:49 2016'
join_quit_row = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: Bye]'
message_row = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'


assert get_hours_minutes(log_open_row) == {}
assert get_hours_minutes(join_quit_row) == {'hour': 0, 'minute': 1}
assert get_hours_minutes(message_row) == {'hour': 0, 'minute': 25}










