#!/usr/bin/python

id_counter = 1

def getName(classObject):

    right = "'"
    left = '.'

    try :
        string = str(classObject.__class__)
        start = string.rfind(left) + 1
        end = string.rfind(right)
        return string[start:end]
    except:
        try :
            return str(classObject.__class__)
        except:
            return "NA"

class Base(object):
	def __init__(self, classTypes, classInstances):
		# used to mimick the global id of the object
		global id_counter
		self.id = id_counter
		id_counter += 1

		self.classTypes = classTypes
		self.classInstances = classInstances

	def JSON(self):
		selfDict = dict(self.__dict__)
		
		# remove our two private types
		del selfDict["classInstances"]
		del selfDict["classTypes"]
		
		data = { getName(self) : selfDict }
		return data

	def generateRelation(self, relationType):
		# checks to see if we have a TestClass type
		# if we don't, create one, if we do, just use existing one

		match = False
		matchID = -1
		matchInstance = None
		for t in self.classInstances:
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
			self.classInstances.append(relationType(self.classTypes, self.classInstances))
			matchID = self.classInstances[len(self.classInstances) - 1].id
			matchInstance = self.classInstances[len(self.classInstances) - 1]
			return { 'type' : getName(matchInstance), 'id' : matchID }
			
		print match, " on ", t

