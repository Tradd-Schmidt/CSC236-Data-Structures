#-------------------------------------------------------------------------------
# Name:        Hopper.py
# Purpose:  It defines a hopper object that contains some coal.
#
# Created:     31/08/2014
#-------------------------------------------------------------------------------

class Hopper( object ):
    '''A Hopper class, which contains coal'''

    MAX_CAPACITY = 100  # how much coal any HOPPER can hold

    def __init__(self):
        '''post: this object will have no coal in it.'''
        self.coal = 0

    def fill_coal( self):
        ''' post: refill the hopper to MAX_CAPACITY'''
        self.coal = self.MAX_CAPACITY

    def amount_coal(self):
        '''access the amount of coal in this hopper'''
        return self.coal

    def drain_coal(self, drain_amount ):
        '''post: the amount of coal in this hopper is decreased by the
            drain_amount only if there is enough to drain'''
        if( self.coal > drain_amount ):
            self.coal = self.coal - drain_amount

    def __str__(self):
        '''convert the information of this hopper into a string '''
        return "hopper contains "+str(self.amount_coal())+" pounds of coal."
