#! /env/bin/python

import pdb

id_counter = 1

class BaseID(object):
	def __init__(self):
		# used to mimick the global id of the object
		global id_counter
		self.id = id_counter
		id_counter += 1


class TestClass(BaseID):
	def __init__(self):
		BaseID.__init__(self)
	
		# name is max 60 chars
		self.name = "This is the name of the test class's major field."
		# title is max 50 chars
		self.title = "Vertical Market 1"

	def JSON(self):
		print(self.__dict__)

class RelationTest(BaseID):
	def __init__(self):
		BaseID.__init__(self)

		self.relation = Relation(TestClass)





classes = [TestClass, RelationTest]

def Relation(classType):
	# checks to see if we have a TestClass type
	# if we don't, create one, if we do, just use existing one
	global classes

	match = False
	for t in classes:
		if isinstance(t, classType):
			match = True
			print "WOOHOO"
			
		print t
		print classType
		pdb.set_trace()

		print match, " on ", t



def run():
	global classes
	
	myClasses = []
	
	for t in classes:
		myClasses.append(t())
		#myClasses[0].JSON()


# do the magic
run()

