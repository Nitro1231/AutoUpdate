import json

test_dict = {
    'ad': 'awd'
}

data = {
    'str': 'str',
    'int': 10,
    'float': 0.0001,
    'bool': False,
    'list': ['a', 10, False],
    'tuple': (0, 10),
    'dict': test_dict,
    # 'set': set(['a', 'b', 'a', 'c']),
    # 'type': type(10),
    # 'error': ValueError,
    'None': None
}


with open('./data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)