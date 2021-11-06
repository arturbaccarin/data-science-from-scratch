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
c = Counter([0, 1, 2, 0])
c = Counter(['a', 'b', 'c', 'a', 'a'])

'''
Sorting:
'''
x = [4, 1, 2, 3, 5]
x = sorted(x)
x = sorted(x, reverse=True)

'''
List Comprehension
'''
even_number = [x for x in range(5) if x%2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_number]

# turn lists into dictionaries
square_dict = {x: x * x for x in range(5)}

increasing_pairs = [(x, y) for x in range(10) for y in (x+1, 10)]

# Ramdomness
import random
random.seed(10) # this ensures we get the same results every time
four_uniform_randoms = [random.random() for _ in range(4)]
random.seed(10)
# set the seed to 10
print(random.random())
# 0.57140259469
random.seed(10)
# reset the seed to 10
print(random.random())
# 0.57140259469 again

random.randrange(10)
random.randrange(3, 9)

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten) # save in the variable withou assignement

## If you need to randomly pick one element from a list
colors = ['yellow', 'red', 'blue']
random.choice(colors)

'''
a sample of elements without
replacement (i.e., with no duplicates), you can use random.sample
'''
lottery = range(99)
random.sample(lottery, 6)

## with replacement
[random.choice(lottery) for _ in range(6)]