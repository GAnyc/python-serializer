#!/usr/bin/python

from base import Base

class TestClass(Base):
	def __init__(self, classTypes, classInstances):
		Base.__init__(self, classTypes, classInstances)
	
		## your defines go below
	
		# name is max 60 chars
		self.name = "This is the name of the test class's major field."
		# title is max 50 chars
		self.title = "Vertical Market 1"
