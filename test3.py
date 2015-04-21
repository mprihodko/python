#!/usr/bin/python
import turtle
import random
class Draw(object):
	border_c="black"
	fill_c="yellow"
	point_st=(0,0)
		
	def __init__(self, point_st):
		self.point_st=point_st
	def draw(self):
		
		turtle.penup()
		turtle.goto(self.point_st)
		turtle.pendown()
		turtle.color(self.border_c, self.fill_c)	
		self._draw()

class Triangle(Draw):	
	def _draw(self):	
		turtle.begin_fill()
		for i in range(3):
			turtle.forward(self. size)
			turtle.left(120)
		turtle.end_fill()
	def __init__(self, size=100, *args):
		self.size=size
		super(Triangle,self).__init__(*args)
class Circle(Draw):	
	def _draw(self):		
		turtle.begin_fill()		
		turtle.circle(self.size)
		turtle.end_fill()		
	def __init__(self, size=100, *args):
		self.size=size
		super(Circle,self).__init__(*args)
class Composite(Draw):	
	def __init__(self, *arg):
		for i in arg:
			self.arg=arg
	def draw(self):
		for i  in self.arg:
			i.draw()
		
tr=Triangle(50, (0,0))
ci=Circle(50, (100,0))
a= Composite(tr,ci)
a.draw()
raw_input("b")
