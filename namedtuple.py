
from collections import namedtuple


Student = namedtuple('Student', ['name', 'age', 'gender'])

S = Student('Nandini', '19', 'male')
print(S.name)
print(S[1])
print(getattr(S, 'gender'))

li = ['Manjeet', '19', 'female']
te = Student._make(li)
print(te)

print(te._asdict())

di = {'name': "Nikhil", 'age': 19, 'gender': '1391997'}
print(Student(**di))
