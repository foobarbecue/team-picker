#!/usr/local/bin/python2.7
# encoding: utf-8
'''
team_picker.picker -- A utility to randomly choose teams

@author:     Aaron Curtis
@license:    Attribution required, other rights not reserved
@contact:    aarongc@nmt.edu
@deffield    updated: 2013-09-20
'''

import random, pdb

players=[Bob, Joe, Ted]

resolutions=[
             'Resolved: Human access to caves must be reduced to protect the resource.',
             'Resolved: The federal government shall establish and publish a national database of caves including locations.',
             'Resolved: Speleogenesis research should focus more on the physics of cave systems than their chemistry.',
             'Resolved: Speleogenesis research should put greater emphasis on hypogene processes.',
             'Resolved: The federal government shall fund the exploration of caves on other planetary bodies.',
             'Resolved: The petroleum industry shall fund basic karst research.',
             'Resolved: Researchers shall be allowed to remove cave material for the purpose of climate research.'
             ]
teams=[]
debates=[]

class Team:
    '''A team, with the players'''
    def __init__(self, max_size, players=[]):
        self.max_size=max_size
        self.players=players
    
    def add_player(self, player):
        self.players.append(player)
        
    def is_full(self):
        return self.max_size==len(self.players)
    
    def __repr__(self):
        return (' and ').join([player for player in self.players])

class Debate:
    '''A debate, with the teams'''
    scheduled_time=None
    
    def __init__(self, resolution, teams):
        self.resolution=resolution
        self.teams=teams

def pick_teams_cx(resolutions=resolutions, team_max_size=2, team_positions=['Affirmative','Negative'], players=players):
    '''Pick teams for a cross-examination debate'''

    #assign players to teams
    random.shuffle(players)
    for player in players:
        #if there are not teams yet or the last team is full 
        if not teams or teams[-1].is_full():
            new_team=Team(players=[player],max_size=team_max_size)
            teams.append(new_team)
        else:
            teams[-1].add_player(player)
            
    #assign teams and resolutions to debates
    random.shuffle(resolutions)
    for resolution in resolutions:
        try:
            aff=teams.pop()
            neg=teams.pop()
            debates.append(Debate(resolution, [aff,neg]))
        except IndexError:
            print "Resolution unassigned, not enough teams: \n    '%s'" % resolution
    display_debates()

def display_debates():
    '''Prints who will debate who'''
    for debate in debates:
        print "%s will debate against %s regarding \n   '%s'" % (debate.teams[0], debate.teams[1], debate.resolution)
