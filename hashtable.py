class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size
	
	def put(self, key, data):
		# there are three situations,
		#1. the hashvalue returned by hashfunction of the slot is empty, just put the key in that slot, and the data in the datalist
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
		#2. the hashvalue returned by the hashfunction of the slot is not empty and is the same of the key , replace the data
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data #replace

			else:
		#3. the hashvalue returned by the hashfunction of the slot is not empty and is different from the key, you need to do rehashing
		# while the rehashing value is not the same as the key and is not empty
				nextslot = self.rehash(hashvalue, len(self.slots))
				while nextslot != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))
		#3.1 the reshashing value is empty
				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
		#3.2 the reshashing value is the same as the key in the current slot
				else:
					self.data[nextslot] = data #replace



	def hashfunction(self, key, size):
		return key%size

	def rehash(self,oldhash,size):
		return (oldhash + 1)%size
