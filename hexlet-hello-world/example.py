from more_itertools import flatten, substrings

coll = [(0, 1), (2, 3)]
# делаем коллекцию плоской
print(list(flatten(coll))) # => [0, 1, 2, 3]

# получаем все подстроки строки
print([''.join(s) for s in substrings('more')])
# => ['m', 'o', 'r', 'e', 'mo', 'or', 're', 'mor', 'ore', 'more']