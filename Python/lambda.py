# dictionaries inside list
people=[
    {"name":"sukku","home":"mokama"},
    {"name":"janu","home":"nellore"},
    {"name":"aamir","home":"katihaar"}
]

# want to print this list in sorted order
# but we cant compare 2 dictonaries we will get <type error if we use print(people.sort())
# there are 2 methods to print dictionaries in sorted order

# first one is using function
'''
def sort_func(person):
    return person["name"] 

people.sort(key=sort_func)

'''
# second using lambda keyword
people.sort(key=lambda person: person["name"])
print(people)