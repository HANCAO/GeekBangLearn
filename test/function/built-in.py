# map reduce filter zip

# help(filter)  # 获取内置函数帮助

# Help on class filter in module builtins:
#
# class filter(object)
#  |  filter(function or None, iterable) --> filter object
#  |
#  |  Return an iterator yielding those items of iterable for which function(item)
#  |  is true. If function is None, return the items that are true.
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for pickling.

# list_filter = [1, 2, 3, 4, 5, 6]
# # print(list(filter(lambda x: x > 3, list_filter)))  # [4, 5, 6]

# help(map)

# Help on class map in module builtins:
#
# class map(object)
#  |  map(func, *iterables) --> map object
#  |
#  |  Make an iterator that computes the function using arguments from
#  |  each of the iterables.  Stops when the shortest iterable is exhausted.
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for pickling.

# list_map = [1, 2, 3]
# print(list(map(lambda x: x + 1, list_map)))  # [2, 3, 4]

# list_map_other = [2, 3, 4]
# print(list(map(lambda x, y: x + y, list_map, list_map_other)))  # [3, 5, 7]

# from functools import reduce
# help(reduce)

# Help on built-in function reduce in module _functools:
#
# reduce(...)
#     reduce(function, sequence[, initial]) -> value
#
#     Apply a function of two arguments cumulatively to the items of a sequence,
#     from left to right, so as to reduce the sequence to a single value.
#     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#     of the sequence in the calculation, and serves as a default when the
#     sequence is empty.
# from functools import reduce
#
# list_reduce = [1, 2, 3]
# print(reduce(lambda x, y: x + y, list_reduce, 1))  # 7  = (((1 + 1) + 2) + 3)

# help(zip)

# Help on class zip in module builtins:
#
# class zip(object)
#  |  zip(iter1 [,iter2 [...]]) --> zip object
#  |
#  |  Return a zip object whose .__next__() method returns a tuple where
#  |  the i-th element comes from the i-th iterable argument.  The .__next__()
#  |  method continues until the shortest iterable in the argument sequence
#  |  is exhausted and then it raises StopIteration.
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for pickling.

# list_zip = [1, 2, 3]
# # list_zip_other = [2, 3, 4]
# # for i in zip(list_zip, list_zip_other):
# #     print(i)
# #
# # # (1, 2)
# # # (2, 3)
# # # (3, 4)

# dict_zip = {'hschen.top': 'blog', 'kuying.club': 'club'}
# # for i in zip(dict_zip.values(), dict_zip.keys()):
# #     print(i)
# #
# # # ('blog', 'hschen.top')
# # # ('club', 'kuying.club')
# #
# # print(dict(zip(dict_zip.values(), dict_zip.keys())))
# # # {'blog': 'hschen.top', 'club': 'kuying.club'}

dict1 = {'a':'aa', 'b':'bb'}
dict2 = zip(dict1.values(),dict1.keys())
print(dict1)
print(dict(dict2))
a = dict(dict2)
print(a)

