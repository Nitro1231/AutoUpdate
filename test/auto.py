import json

with open('./test/org.json', 'r', encoding='utf-8') as f:
    org_data = json.load(f)

# print(org_data)

new_dict = {}

for k, v in org_data.items():
    if k not in new_dict and v['type'] != 'dict':
        new_dict[k] = v['default']
        print(v)


print(new_dict)