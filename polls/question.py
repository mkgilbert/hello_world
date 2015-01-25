"""
This file is for testing how python can use directories as modules. 
Because Django uses this feature, I want to make sure I understand how
it works. For example, calling polls.question when there is a directory
called "polls" and a file in it called "question"

"""

class Question:
	
	def __init__(self, question):
		self.question = question
		
	def ask(self):
		print(self.question)
		
	def __str__(self):
		return question
		
	