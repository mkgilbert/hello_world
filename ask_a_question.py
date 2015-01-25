"""
Trying to use a feature of a class inside another directory...
"""

from polls.question import Question

q = Question("What do you want?")
q.ask()