import pickle
d=dict(name='bob',age='12')
print(pickle.dumps(d))

import json
d=dict(name='bob',age='12')
print(json.dumps(d))
p='{"name": "bob", "age": "12"}'
print(json.loads(p))