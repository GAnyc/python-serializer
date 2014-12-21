#!/usr/bin/python

from testClass import TestClass
from base import Base

class RelationTest(Base):
	def __init__(self, classTypes, classInstances):
		Base.__init__(self, classTypes, classInstances)

		## your defines go below

		self.relation = self.generateRelation(TestClass)
