from Command import Command
import unittest

class Test_Command(unittest.TestCase):

	def setUp(self):
		c = Command("add", "a")
		def x():
			return True
		c.set_action(x)
		self.c = c
		
	def tearDown(self):
		pass
	
	def test_callable(self):
		self.assertTrue(callable(self.c.action), "commands action is not callable")
	
	def test_empty_params(self):
		self.assertTrue(self.c.execute(), "Command: empty params execute failed")
	
	def test_single_params(self):
		def x(a):
			return a * 10
		self.c.set_action(x)
		self.c.add_param("foo")
		self.c.set_param(2)
		self.assertEquals(self.c.execute(), 20, "Command: single params execute failed")
	
	def test_multi_params(self):
		def x(a, b, g):
			return a * b * g * 10
		self.c.set_action(x)
		self.c.add_param("foo")
		self.c.add_param("foo")
		self.c.add_param("foo")
		self.c.set_param(2)
		self.c.set_param(3)
		self.c.set_param(4)
		self.assertEquals(self.c.execute(), 240, "Command: multi params execute failed")
	
	def test_missing_params(self):
		def x(a, b, g):
			return a * b * g * 10
		self.c.set_action(x)
		self.c.add_param("foo")
		self.c.add_param("foo")
		self.c.add_param("foo")
		self.c.set_param(2)
		self.c.set_param(3)
		self.assertFalse(self.c.execute(), "Command: missing params execute should have failed")
	
	def test_too_many_params(self):
		def x(a):
			return a * 10
			
		self.c.set_action(x)
		self.c.add_param("foo")
		self.c.add_param("foo")
		self.c.add_param("foo")
		self.c.set_param(2)
		self.c.set_param(3)
		self.assertFalse(self.c.execute(), "Command: too many params execute should have failed")