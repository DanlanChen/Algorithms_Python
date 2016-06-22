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

	def get(self, key):
		# there are some auguments: startslot(the initial hashvalue of the key by the hashfunction), data(the corresponding data of the key)
		#stop( a boolean value indicating whether to stop or not, position (the position you indicated in the slot)),#found(indicator)

		startslot = self.hashfunction(key, len(self.slots))
		position = startslot
		stop = False
		found = False
		data = None
		while position is not None and not stop and not found :
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key,data)

