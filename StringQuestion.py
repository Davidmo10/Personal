from Confirmation import Confirmation


class StringQuestion(Confirmation):
	
	def __init__(self, question = None, confirmation = None):
	  if (question == None or confirmation == None):
	    raise ValueError('Missing question and clue')#Placeholder
	  
	  self.question = question
	  self.confirmation = confirmation
	  
	  
	def validate(self, answer = None):
	 

	def display(self):
		print(self.question)
