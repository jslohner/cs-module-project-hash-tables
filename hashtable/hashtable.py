class HashTableEntry:
	"""
	Linked List hash table key/value pair
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

	def __repr__(self):
		return f'{self.key} --- {self.value}'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
	"""
	A hash table that with `capacity` buckets
	that accepts string keys

	Implement this.
	"""

	def __init__(self, capacity):
		self.capacity = capacity
		self.hash_count = 0
		self.hash_data = [None] * capacity


	def get_num_slots(self):
		"""
		Return the length of the list you're using to hold the hash
		table data. (Not the number of items stored in the hash table,
		but the number of slots in the main list.)

		One of the tests relies on this.

		Implement this.
		"""
		return len(self.hash_data)


	def get_load_factor(self):
		"""
		Return the load factor for this hash table.

		Implement this.
		"""
		# load factor = number of elements stored in the hash table / number of slots
		return self.hash_count / self.capacity


	def fnv1(self, key):
		"""
		FNV-1 Hash, 64-bit

		Implement this, and/or DJB2.
		"""
		# fnv offset basis
		hash = 14695981039346656037
		for c in key:
			# fnv prime number
			hash *= 1099511628211
			# hash xor data
			hash ^= ord(c)
		return hash & 0xffffffffffffffff


	def djb2(self, key):
		"""
		DJB2 hash, 32-bit

		Implement this, and/or FNV-1.
		"""
		hash = 5381
		for c in key:
			hash = ((hash << 5) + hash) + ord(c)
		return hash & 0xffffffff


	def hash_index(self, key):
		"""
		Take an arbitrary key and return a valid integer index
		between within the storage capacity of the hash table.
		"""
		return self.fnv1(key) % self.capacity
		# return self.djb2(key) % self.capacity


	def put(self, key, value):
		"""
		Store the value with the given key.

		Hash collisions should be handled with Linked List Chaining.

		Implement this.
		"""
		# get index and set hash_data at that index to [value]
		# index = self.hash_index(key)
		# self.hash_data[index] = value
		# ---
		if self.get_load_factor() > 0.7:
			self.resize(self.capacity * 2)
		index = self.hash_index(key)
		hash_entry = HashTableEntry(key, value)
		if self.hash_data[index]:
			if self.hash_data[index].key == key:
				self.hash_data[index] = None
				self.hash_data[index] = hash_entry
			else:
				self.hash_count += 1
				hash_entry.next = self.hash_data[index]
				self.hash_data[index] = hash_entry
		else:
			self.hash_count += 1
			self.hash_data[index] = hash_entry
		if self.get_load_factor() > 0.7:
			self.resize(self.capacity * 2)

	def delete(self, key):
		"""
		Remove the value stored with the given key.

		Print a warning if the key is not found.

		Implement this.
		"""
		# get index and set hash_data at that index to [None]
		# if self.get(key):
		# 	index = self.hash_index(key)
		# 	self.hash_data[index] = None
		# else:
		# 	print('warning - key is not found')
		# ---
		if self.get(key):
			index = self.hash_index(key)
			current = self.hash_data[index]
			if current.key == key:
				self.hash_data[index] = current.next
				return current
			prev = current
			current = current.next
			while current:
				if current.key == key:
					prev.next = current.next
					return current
				prev = current
				current = current.next
		else:
			print('warning - key is not found')


	def get(self, key):
		"""
		Retrieve the value stored with the given key.

		Returns None if the key is not found.

		Implement this.
		"""
		# get index and return value of hash_data at that index
		# index = self.hash_index(key)
		# return self.hash_data[index]
		# ---
		index = self.hash_index(key)
		current = self.hash_data[index]
		while current:
			if current.key == key:
				return current.value
			current = current.next
		return None


	def resize(self, new_capacity):
		"""
		Changes the capacity of the hash table and
		rehashes all key/value pairs.

		Implement this.
		"""
		self.hash_count = 0
		self.capacity = new_capacity
		self.prev_hash_data = self.hash_data
		self.hash_data = [None] * new_capacity
		for hash in self.prev_hash_data:
			if hash:
				if hash.next:
					current = hash
					while current:
						self.put(current.key, current.value)
						current = current.next
				else:
					self.put(hash.key, hash.value)


if __name__ == "__main__":
	ht = HashTable(8)

	ht.put("line_1", "'Twas brillig, and the slithy toves")
	ht.put("line_2", "Did gyre and gimble in the wabe:")
	ht.put("line_3", "All mimsy were the borogoves,")
	ht.put("line_4", "And the mome raths outgrabe.")
	ht.put("line_5", '"Beware the Jabberwock, my son!')
	ht.put("line_6", "The jaws that bite, the claws that catch!")
	ht.put("line_7", "Beware the Jubjub bird, and shun")
	ht.put("line_8", 'The frumious Bandersnatch!"')
	ht.put("line_9", "He took his vorpal sword in hand;")
	ht.put("line_10", "Long time the manxome foe he sought--")
	ht.put("line_11", "So rested he by the Tumtum tree")
	ht.put("line_12", "And stood awhile in thought.")

	print("")

	# Test storing beyond capacity
	for i in range(1, 13):
		print(ht.get(f"line_{i}"))

	# Test resizing
	old_capacity = ht.get_num_slots()
	ht.resize(ht.capacity * 2)
	new_capacity = ht.get_num_slots()

	print(f"\nResized from {old_capacity} to {new_capacity}.\n")

	# Test if data intact after resizing
	for i in range(1, 13):
		print(ht.get(f"line_{i}"))

	print("")
