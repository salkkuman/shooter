class Event(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.event=1
        self.trigger=100
        self.time=0
        
    def next(self):
        self.event+=1
        self.trigger=100
        
    def reset(self):
        self.event=1
        self.trigger=100
        self.time=0