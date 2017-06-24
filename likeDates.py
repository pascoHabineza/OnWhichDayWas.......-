

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False
    

    def isBefore(self,d2):
        '''this function returns True if self date is before d2 or returns false when otherwise
        or when self and d2 are the same dates
        '''
        if self.year<d2.year:
            return True

        if self.month<d2.month and self.year==d2.year:
            return True

        if self.day<d2.day and self.year==d2.year and self.month==d2.month:
            return True

        return False 

    def isAfter(self,d2):
        ''' this method returns True when the self date is after d2 date, but returns false when otherwise
        or when d2 and self are the same dates
        '''

        if self.year>d2.year:
            return True
        if self.month>d2.month and self.year==d2.year:
            return True

        if self.day>d2.day and self.year==d2.year and self.month==d2.month:
            return True
        return False

    def tomorrow(self):
        ''' this method adds one day to the calling object so that it represents one day after the orginal day 
        it represented
        '''
        fdays= 28+ self.isLeapYear()

        DIM=[0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        self.day=self.day+1

        if self.day>DIM[self.month]:
            self.month=self.month+1
            self.day=1

            if self.month>12:
                self.year=self.year+1
                self.month=1

    def yesterday(self):
        ''' moves the self date 1 day back
        '''

        fdays=28+self.isLeapYear()
        DIM=[0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        self.day=self.day-1

        if self.day==0:
            self.month=self.month-1
            self.day= DIM[self.month]

            if self.month==0:
                self.month=12
                self.year=self.year-1
                self.day=DIM[self.month]

    def addNDays(self,N):
        ''' this method moves self date ahead N days'''
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self,N):
        ''' this method moves self back N days'''
        print(self)

        for i in range(N):
            self.yesterday()
            print(self)
    
    def __eq__(self, d2):
        """ Overrides the == operator so that it declares two of the same dates in history as ==
            This way , we don't need to use the awkward d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    
    def diff(self,d2):
        ''' this method returns the number of days between self days and d2 days
        '''
        self_copy= self.copy()
        d2_copy= d2.copy()
       
       

        

        p = 0
        if d2.isAfter(self):
            while d2_copy.isAfter(self_copy):
                d2_copy.yesterday()
                p-= 1
        if d2.isBefore(self):
            while d2_copy.isBefore(self_copy):
                d2_copy.tomorrow()
                p += 1
        return p
        
    def dow(self):
        ''' this method returns the day of the week of the object that calls'''
        W=['Wednesday','Thrusday','Friday','Saturday','Sunday','Monday','Tuesday']
        d= Date(11,9,2016)
        k= self.diff(d)
        m= k%7
        return W[m]

            






        











# +++++  be sure you add more methods (the functions internal to the Date class)  ABOVE  this line  +++++


# THIS IS A GOOD PLACE TO DEFINE OBJECTS (VARIABLES) !!!
#
# ... because they need to be redefined each time you
#     change this class and run this file
#
# ... defining them here saves you from having to re-type them :-) 
#

d = Date(11,9,2016)
ny = Date(1,1,2017)

# feel free to add more, e.g., your birthday, etc.


