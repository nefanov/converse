import os, sys
import pprint

from proc import *
## Indexation disclaimer:
# according to the previous research, identifiers represents symmetric group, thus, reenumeration is submitted:
# On the first pass stage, DFS-based numbers will be generated and saved into the map number <-> real_identifier (OrderedList(LogSearch)). Thus, normalization of trees will be made: 
#1
#|\
#2 5
#|\
#3 4
#This class represents the stack with stack-frame mechanism
class stack:
	def __init__(self):
		self.bp = 0
		self.sp = 0
		self.lr = 0 # for return pos - ARM link register analogue;)
		self.data = list()

	#In usage, the stack is represented as indexed structure,  from 0 to len-1:
	def __getitem__(self, idx):
		return self.data[idx]

	def __setitem__(self, k, v):
		self.data[k] = v

	#Neverteless, FILO methods is also presented:
	def push(self, v):
		self.data.append(v)
		self.sp += 1 #STRIA - manner

	def pop(self):
		self.sp -= 1 #LDRDB - manner
		return self.data.pop()
	# stackframe routines is constructed like in ARM processors:
	# save the bp into lr and set bp = sp
	def frame(self):
		self.lr = self.bp
		self.bp = self.sp

	def unwind(self):
		self.bp = self.lr

	#metadata is on the first position of the frame
	def frame_update_metadata(self, v):
		try:
			self[self.bp] = v
		except:
			self.push(v)

	def frame_get_metadata(self):
		try:
			return self[self.bp]
		except:
			return 'no_metadata'

# test
def test():
	s = stack()
	s.push(1)
	s.push(2)
	print(s.pop())

	
def test_frame():
	s=stack()
	s.push(1)
	s.frame()
	s.frame_update_metadata('azaza')
	print(s[0],s[1])

	print(s.frame_get_metadata()) # expect 2
	s.push(5)
	print(s.pop())
	print(s.pop())
