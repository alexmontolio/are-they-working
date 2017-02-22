from app import db

class Elevator(db.Model):
	building= db.Column(db.String(30), primary_key=True)
	left	= db.Column(db.Boolean)
	right 	= db.Column(db.Boolean)
	
	def __init__(self, building, left, right):
		self.building 	= building
		self.left 		= left
		self.right 		= right
	
	def __repr__(self):
		return "<{} | Left: {}, Right: {}".format(self.building,
												  str(self.left),
												  str(self.right))
		
class Outage(db.Model):
	id 			= db.Column(db.Integer, primary_key=True)
	elevator 	= db.Column(db.String(10), index=True)
	start_time 	= db.Column(db.DateTime)
	end_time 	= db.Column(db.DateTime)
	
	def __init__(self, id, elevator, start_time):
		self.id 		= id
		self.elevator 	= elevator
		self.start_time = start_time
		self.end_time 	= None
		
	def __repl__(self):
		return "<OUTAGE | Elevator: {}, Start Time: {}, "\
			   "End Time: {}>".format(self.elevator,
									  self.start_time,
									  self.end_time)
									  
	def __add__(self):
		#Idea will be to add the total outage time
		#based on the DateTime
		pass
		
	def __sub__(self):
		#Same concept for add
		pass

class Residents(db.Model):
	id 		= db.Column(db.Integer, primary_key=True)
	name 	= db.Column(db.String(60), index=True, unique=True)
	email 	= db.Column(db.String(50), index=True, unique=True)
	
	def __init__(self, id, name, email):
		self.id 	= id
		self.name 	= name
		self.email 	= email
	
	def __repl__(self):
		return "<Resident | Name: {}, Email: {}>".format(self.name,
														 self.email)
	
class Management(db.Model):
	id		= db.Column(db.Integer, primary_key=True)
	name	= db.Column(db.String(60), index=True, unique=True)
	position= db.Column(db.String(30), index=True, unique=False)
	email	= db.Column(db.String(50), index=True, unique=True)
	
	def __init__(self, id, name, email, position=""):
		self.id 		= id
		self.name 		= name
		self.email 		= email
		self.position 	= position
	
	def __repl__(self):
		return "<Management | Name: {}, Email: {}>".format(self.name,
														   self.email)