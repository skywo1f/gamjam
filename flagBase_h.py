# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 05:28:59 2021

@author: iviti
"""
from constants_h import *
from utilities_h import *

class flagBase:
    team = 0
    x = 0
    y = 0
    teamCount = [0]*nTeams                                  #how many players of each team are near the goal
    
    def __init__(self,x,y,team):
        self.x = x
        self.y = y
        self.team = team
        
    def updateTeam(self,npcList):
        for i in range(nTeams):                     #first reset the list
            self.teamCount[i] = 0
            
        for i in range(len(npcList)):
            r = getRange(self.x,self.y,npcList[i].x,npcList[i].y)
            if r < baseRange:
                self.teamCount[npcList[i]] = self.teamCount[npcList[i]]  + 1
        maxNum = 0
        for i in range(nTeams):                                         #could technically be folded into the last nteams loop but im putting it here for simplicity
            if self.teamCount[i] > maxNum:
                self.team = i
                maxNum = self.teamCount[i]
                
    def drawBase(self):
        pygame.draw.rect(screen, GREY, [1 + self.x, 1 + self.y, 10, 10], 2)                         #GREY will eventually be switched with teamColors
