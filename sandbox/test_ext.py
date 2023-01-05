#!/usr/bin/env python3


class Pierre():
	def option1(self):
		print("a")
	def option2(self):
		print("C")

class pmoney(Pierre):
	def option1(self):
		print("");
		Pierre().option1()
		print("b")

p = pmoney()
p.option1()
p.option2()




