


# the_string = "this is a string"

# the_integer = 42

# the_interpolated_string = f'another string with this number: { the_integer }'

# print( the_interpolated_string )





the_float = 42.4134132423

the_boolean = True

another_boolean = False

the_nothing = None

the_integer = 42

def show_us_something( one_param, two_param = 'two' ):
    print( f'the first argument was { one_param }' )
    print( f'and the second one was { two_param }' )

    return 'this can be assigned to a variable!'
    
# new_variable = show_us_something( 'meow' )

# print( new_variable )



# Data structures!

# List => formally known as the "array"

# the_list = [ 1, 2, 3, the_nothing, ['meow', 'woof'], 'the something' ]

# print( the_array[4] ) # => another list!



# Dictionary => formally known as the "object"

the_dict = { 'key': 'value', 'meow': 'cat sound', 'fun': True  }

# print( the_dict['meow'] ) # => 'cat sound ' 



# Tuple!  Just like a list, but you can't change anything in it, i.e. it's 
# immutable

the_tuple = ( 'first', 'second', 'third' )

#the_tuple[0] = 'not first' # => this breaks, there is no changing a tuple.


# Sets!  # => an unordered collection of unique values

the_set = { 1, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6 }

another_set = set( [ 1,2,3,4,5,5,5,5,5,5 ] )

# print( another_set )



# Logic! 
# some_variable = False

# if not some_variable:
#     print( 'hello world!' )






# the_list = [ 1, 2, 3, 'the something' ]

# Looping
#    a variable we declare to represent on element
#    in whatever we're itering over
#        |
#        V
# for meowmeow in the_list:
#     print( meowmeow )



# List Comprehensions

the_list = [ 1, 2, 3, 4 ]

#             what will end up
#             in the new list
#                   |
#                   V
another_list = [ element for element in the_list ]
#                              ^
#                              |
#                       a variable of our own declaration
#                      choosing which will
#                       repesent one of the
#                       elements in the list



people = [
    { 'name': 'adam', 'wizard': False },
    { 'name': 'emiley', 'wizard': False },
    { 'name': 'ix', 'wizard': True },
    { 'name': 'amelie', 'wizard': True }
]

only_wizards = [ p['name'] for p in people if p['wizard'] == True ]

print( only_wizards )
