"""
Trying to use a feature of a class inside another directory...
"""

from polls.question import Question

q = Question("How are you?")
q.ask()