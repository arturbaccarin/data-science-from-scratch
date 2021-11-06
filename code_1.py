from collections import defaultdict

'''
A defaultdict is like a regular dictionary, except that when you try
to look up a key it doesn’t contain, it first adds a value for it using a
zero-argument function you provided when you created it.
'''

my_dict = {}
my_dict = defaultdict(int)
my_list = ['a', 'b', 'c']
for item in my_list:
    my_dict[item] += 1


from collections import Counter
'''
A Counter turns a sequence of values into a defaultdict(int)-like object
mapping keys to counts:
'''
