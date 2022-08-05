from django.utils import timezone
'''
                #django.utils.timezone
                #1.utc
                #2.get_fixed_timezone(offset)
                #3.get_default_timezone()¶
                #4.get_default_timezone_name()¶
                #5.get_current_timezone()¶
                #6.get_current_timezone_name()¶
                #7.activate(timezone)¶
                #8.deactivate()¶
                #9.override(timezone)¶
                #10.localtime(value=None, timezone=None)¶
                #11.localdate(value=None, timezone=None)¶
                #12.now()¶
                #13.is_aware(value)¶
                #14.is_naive(value)¶
                #16.make_aware(value, timezone=None, is_dst=None)
                #15.make_naive(value, timezone=None)¶

 '''
from django.db import models
from django.conf import settings

class Post(models.Model):
    author =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    '''
    #Ref:https://learndjango.com/tutorials/django-best-practices-referencing-user-model
    #User authentication having a built-in solution Django
    #reference a User using 3 methods
    #1.User - The default way is to access User directly
    #2.AUTH_USER_MODEL - If you've already created a custom user model
    #in an app called accounts (though this could also be called users or
    #anything else, really), you'd reference it in your settings.py
        # settings.py
    #    AUTH_USER_MODEL = `accounts.CustomUser`
    #3.get_user_model() - returns the currently active user model: either
     #a custom user model specificed in AUTH_USER_MODEL or else the default
     #built-in User.

    #on_delete=models.CASCADE
    #on_delete doesn’t create an SQL constraint in the database
    #The possible values for on_delete are found in django.db.models:
     #   1.CASCADE
      #  2.PROTECT
      #  3.RESTRICT
      #  4.SET_NULL
      #  5.SET_DEFAULT
      #  6.SET()
      #  7.DO_NOTHING

    '''
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    ''' # null=True sets NULL (versus NOT NULL) on the column in your DB. Blank
    # values for Django field types such as DateTimeField or ForeignKey will be 
    # stored as NULL in the DB.

    #blank determines whether the field will be required in forms. This includes 
    #the admin and your custom forms. If blank=True then the field will not be 
    #required, whereas if it's False the field cannot be blank.

    #The combo of the two is so frequent because typically if you're going to 
    #allow a field to be blank in your form, you're going to also need your 
    #database to allow NULL values for that field. The exception is CharFields 
    #and TextFields, which in Django are never saved as NULL. Blank values are 
    #stored in the DB as an empty string ('').
    '''

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        '''
#class Person:
    #def __init__(self,name,age):
        #self.name = name
        #self.age = age

    #def myfunc(self):
        #print('Hello my name is %s and i am %d years old'%(self.name,self.age))

#p1 = Person('Rashad', 27)
#p1.myfunc()
'''


