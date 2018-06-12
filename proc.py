import sys, os
import pprint

# This class describes single node in the IR tree
class proc:
	def __init__(self, p,g,s,pp, call='fork'):
		self.p = p
		self.g = g
		self.s = s
		self.pp = pp
		self.call = call

	def getpid(self):
		return self.p

	def getpgid(self):
		return self.g

	def getsid(self):
		return self.s

	def getppid(self):
		return self.pp
	
	def getcall(self):
		return self.call

	def setpid(self, p=1):
		self.p = p

	def setpgid(self, g=1):
		self.g = g

	def setsid(self, s=1):
		self.s = s

	def setppid(self, pp=1):
		self.pp = pp

	def setcall(self, call='fork'):
		self.call = call

