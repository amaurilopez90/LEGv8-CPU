"""
	ca$h Simulation Project
	github.com/amaurilopez90/Computer-Architure/ca$h
	The below code is meant to simulate a cache memory system in an effort to analyze
	the different kinds of results given using certain replacement polcies
"""

#Set up our "Set" class for the cache, not to be confused with the set data structure
class Set(object):
	index = [""] * 16 #which address within the set 
	offset = "" #set index to go to
	tag = "" #data

	def __init__(self, offset, index, tag):
		self.offset = offset
		self.index = index
		self.tag = tag

def main():
	data = []
	N = 32
	K = 2

	HIT = 0
	MISS = 0

	#Read file stream and store every byte as a string of bits in a list
	#File stream used for this example is TRACE2.DAT -> change for various trace files as such
	with open("traceFiles/TRACE2.DAT", "rb") as file:
		byte = file.read(1)
		while byte:
			byte = ord(byte)
			byte = bin(byte)[2:].rjust(8, '0')
			data.append(byte)
			byte = file.read(1)


	reorrientedData = []
	i = 0

	#reorrient the bits
	while i < len(data) - 2:
		reorrientedData.append(data[i+2] + data[i+1] + data[i])
		i += 3

	#get ready to hold the data as a list of objects, keep track of the offsets
	dataObjects = [] 
	offsets = []

	for entry in reorrientedData:
		offset = entry[17:21] 
		offsets.append(offset)
		index = entry[13]
		tag = entry[0:13]
		dataObject = Set(offset, index, tag)
		dataObjects.append(dataObject)

	#transfer the offset values into a set in order to remove all of the duplicates
	# offsetList = set(offsets)

	# #get it back into a list
	# offsetList = list(offsetList)

	#create the cache with the list of Set objects
	cache = []
	i = 0
	while i < N:
		cache.append(Set(offsets[i], [""]*K, ""))
		i += 1

	#Uncomment only one section of the below code depending on which replacement policy you wish to analyze

	#Uncomment this portion to use Least-Recently-Used Replacement Policy
	# #LRU
	# for entry in dataObjects:
	# 	for cacheItem in cache:
	# 		#first check the offsets
	# 		if entry.offset == cacheItem.offset:
	# 			if cacheItem.index[0] == "":
	# 				cacheItem.index[0] = entry.tag
	# 				MISS += 1
	# 			elif cacheItem.index[1] == "":
	# 				cacheItem.index[1] = entry.tag
	# 				MISS += 1
	# 			elif cacheItem.index[0] == entry.tag:
	# 				#if HIT, pop index and replace it
	# 				cacheItem.index.pop(0)
	# 				HIT += 1
	# 				cacheItem.index.append(entry.tag)
	# 			elif cacheItem.index[1] == entry.tag:
	# 				cacheItem.index.pop(1)
	# 				HIT += 1
	# 				cacheItem.index.append(entry.tag)
	# 			else:
	# 				cacheItem.index.pop(0)
	# 				cacheItem.index.append(entry.tag)
	# 				MISS += 1

	#Uncomment this portion to use First-In-First-Out Replacement Policy
	#FIFO
	# for entry in dataObjects:
	# 	for cacheItem in cache:
	# 		if entry.offset == cacheItem.offset:
	# 			if cacheItem.index[0] == "":
	# 				cacheItem.index[0] = entry.tag
	# 				MISS += 1
	# 			elif cacheItem.index[1] == "":
	# 				cacheItem.index[1] = entry.tag
	# 				MISS += 1
	# 			elif cacheItem.index[0] == entry.tag:
	# 				HIT += 1
	# 			elif cacheItem.index[1] == entry.tag:
	# 				HIT += 1
	# 			else:
	# 				cacheItem.index.pop(0)
	# 				cacheItem.index.append(entry.tag)
	# 				MISS += 1

	#Print out results
	total = MISS + HIT
	print("Misses: %d\nHits: %d" % (MISS, HIT))
	print("Miss Rate: %f \nHit Rate: %f" % ((MISS/total*10), (HIT/total*10)))
	print("Total Number of References = %d" % (total*10))

#Run main
main()

