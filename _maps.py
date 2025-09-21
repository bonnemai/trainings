_map1={'a':1,'b':2,'c':3}
_map2={'b':3,'c':4,'d':5}

_map3={**_map1,**_map2}
print(_map3)  # {'a': 1, 'b': 3,
_map4=_map1|_map2
print(_map4)  # {'a': 1, 'b': 3,