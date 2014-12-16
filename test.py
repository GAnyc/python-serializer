#! /env/bin/python

import pdb

id_counter = 1

class Base(object):
	def __init__(self):
		# used to mimick the global id of the object
		global id_counter
		self.id = id_counter
		id_counter += 1

	def JSON(self):
		data = { getName(self) : self.__dict__ }
		print(data)

class TestClass(Base):
	def __init__(self):
		Base.__init__(self)
	
		# name is max 60 chars
		self.name = "This is the name of the test class's major field."
		# title is max 50 chars
		self.title = "Vertical Market 1"


class RelationTest(Base):
	def __init__(self):
		Base.__init__(self)

		self.relation = relation(TestClass)


def relation(relationType):
	# checks to see if we have a TestClass type
	# if we don't, create one, if we do, just use existing one
	global classTypes
	global classInstances

	match = False
	matchID = -1
	matchInstance = None
	for t in classInstances:
		if isinstance(t, relationType):
			match = True
			matchID = t.id
			matchInstance = t
			break

	if match:
		# if it already exists just use it
		print "Instance of ", relationType, " was found."
		return { 'type' : getName(t), 'id' : matchID }
	else:
		# otherwise create it, add it to our instances, and use it
		print "Instantiating type ", relationType
		classInstances.append(relationType())
		matchID = classInstances[len(classInstances) - 1].id
		matchInstance = classInstances[len(classInstances) - 1]
		return { 'type' : getName(matchInstance), 'id' : matchID }
		
	print match, " on ", t


def getName(classObject):
	# it's an object
	#right = ""
	#left = ""
	#if classObject.__name__.find(" object at "):
	#	right = ' '
	#	left = '.'
	#else:

	right = "'"
	left = '.'

	try :
		start = classObject.__class__.rfind(right)
		end = classObject.__class__.rfind(left)
		#return classObject.__class__
		return classObject.__class__[start:end]
	except:
		try :
			return classObject.__class__
		except:
			return "NA"


def run():
	global classTypes
	global classInstances
	
	classInstances = []
	
	for t in classTypes:
		found = False
		for i in classInstances:
			if isinstance(i, t):
				found = True
				break

		if not found:
			print "Runner instantiating type ", t
			classInstances.append(t())
			
	print len(classInstances), " - RESULTS:"
	for t in classInstances:
		t.JSON()

classInstances = []

# above this line should be standardized stuff
##############################################


classTypes = [RelationTest, TestClass]

# do the magic
run()

