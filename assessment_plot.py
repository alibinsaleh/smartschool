from matplotlib import pyplot as plt
from enum import Enum, auto


class Assessment(Enum):
    THEORITICAL_PARTICIPATION = auto()
    PRACTICAL_PARTICIPATION = auto()
    THEORITICAL_QUIZ = auto()
    PRACTICAL_QUIZ = auto()
    PROJECTS = auto()
    VIOLATION = auto()


assess_list = ['THEORITICAL_PARTICIPATION',
   'PRACTICAL_PARTICIPATION',
   'THEORITICAL_QUIZ',
   'PRACTICAL_QUIZ', 
   'PROJECTS',
   'VIOLATION']

values = [10, 9, 7, 10, 5, 1]
# plt.figure(figsize=(12, 6))
# plt.plot(assess_list, values)
fig, ax = plt.subplots()
ax.pie(values, labels=assess_list, autopct='%1.1f%%')
plt.show()
