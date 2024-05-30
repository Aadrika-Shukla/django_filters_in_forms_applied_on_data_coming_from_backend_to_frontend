''' FOR CREATING USER DEFINED FILTERS YOU NEED TO CREATE A TEMPLATETAGS PACKAGE INSIDE APP THE IN THAT CRAETE A 
FILE FOR  WRITING USER DEFINED FILTERS FOR WRITING A USER DEFINED FILTERS YOU NEED TO IMPORT FROM 
DJANGO IMPORT TEMPLATE PACKAGE FROM TEMPLATE PACKAGE IMPORT LIBRARY CLASS AND THEN CREATE A OBJECT AS FILTER IS 
LIBRARY CLASS OBJECT  '''



from django import template   #IMPORTING TEMPLATE PACKAGE

register=template.Library()      #CREATING A OBJECT(here register is my object name) FOR LIBRARY CLASS


def swap(value):
    return value.swapcase()

@register.filter(name='remove')                 # method 2 declaring decorator used when we want to keep same name of our filter as our function name we need to give name='in strings filter name'
def remove(value,char):
    return value.replace(char,' ')

register.filter('swapcase',swap)  # method 1 to register the user defined filter (name of the filter,function to be called when we do perform operations on name of the filter given)

register.filter('remove',remove)  # method 1 to register the user defined filter (name of the filter,function to be called when we do perform operations on name of the filter given)