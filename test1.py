#!/usr/bin/python
import turtle
turtle.left(60)
def func_a(points, color):
	turtle.color(color)
	turtle.up()
	turtle.goto(points[0][0],points[0][1])
	turtle.down()
	turtle.begin_fill()
	turtle.goto(points[1][0],points[1][1])
	turtle.goto(points[2][0],points[2][1])
	turtle.goto(points[0][0],points[0][1])
	turtle.end_fill()
def func_b(p1,p2):
	return((p1[0]+p2[1])/2,(p1[1]+p2[1]/2))
def func_c(points, degree):
	arrayColor=["red","blue","green"]
	func_a(points, arrayColor)
	if degree>0:
		func_b(points[0], func_c(points[0], points[1]),func_c(points[0], points[2]))
func_a(100, 3)
raw_input("q")
