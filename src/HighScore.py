'''
Created on 15.7.2012

@author: salama
'''

class HighScore(object):
    '''
    classdocs
    '''


    def __init__(self, score, name):
        '''
        Constructor
        '''
        self.score = score
        self.name = name
    #compares first score and then name
    def compare(self, other):
        if(self.compare2 == -1):
            if(self.compare3(other) == -1):
                return 1
            else:
                self.compare3(other)
        return self.compare2
    def compare2(self, other):
        #1 tarkoittaa etta on suurempi ja 0 pienempaa
        if(self.score > other.score):
            return 1
        if(self.score < other.score):
            return 0
        return -1
        
    def compare3(self, other):
        #1 tarkoittaa etta on suurempi ja 0 pienempaa
        if(self.name > other.name):
            return 1
        if(self.name < other.name):
            return 0
        return -1
#compares first score and then name
def compare(item, other):
    if(item.compare2 == -1):
        if(item.compare3(other) == -1):
            return 1
        else:
            item.compare3(other)
    return item.compare2
def compare2(item, other):
    #1 tarkoittaa etta on suurempi ja 0 pienempaa
    if(item.score > other.score):
        return 1
    if(item.score < other.score):
        return 0
    return -1
    
def compare3(item, other):
    #1 tarkoittaa etta on suurempi ja 0 pienempaa
    if(item.name > other.name):
        return 1
    if(item.name < other.name):
        return 0
    return -1
