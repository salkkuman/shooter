class Event(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.event=0
        self.trigger=100
        self.time=0
        
    def next(self):
        self.event=0
        self.trigger=100
        