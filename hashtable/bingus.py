class HashTableEntry:
	"""
	Linked List hash table key/value pair
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None


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
		# Your code here


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
		index = self.hash_index(key)
		# print(index)
		# self.hash_data[index] = value
		# ---
		hash_entry = HashTableEntry(key, value)
		if self.hash_data[index]:
			# print(self.hash_data[index].next)
			if self.hash_data[index].next:
				hash_entry.next = self.hash_data[index].next
				self.hash_data[index].next = hash_entry
			else:
				self.hash_data[index].next = hash_entry
		else:
			self.hash_data[index] = hash_entry
			# print(self.hash_data[index].value)


	def delete(self, key):
		"""
		Remove the value stored with the given key.

		Print a warning if the key is not found.

		Implement this.
		"""
		# get index and set hash_data at that index to [None]
		if self.get(key):
			index = self.hash_index(key)
			self.hash_data[index] = None
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
		if self.hash_data[index].next:
			return self.hash_data[index].next.value
		else:
			return self.hash_data[index].value


	def resize(self, new_capacity):
		"""
		Changes the capacity of the hash table and
		rehashes all key/value pairs.

		Implement this.
		"""
		# Your code here

ht = HashTable(8)
ht.put("key-0", "val-0")
ht.put("key-1", "val-1")
ht.put("key-2", "val-2")
ht.put("key-3", "val-3")
ht.put("key-4", "val-4")
ht.put("key-5", "val-5")
ht.put("key-6", "val-6")
ht.put("key-7", "val-7")
ht.put("key-8", "val-8")
ht.put("key-9", "val-9")
print(ht.get("key-0"))
