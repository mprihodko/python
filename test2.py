#!/usr/bin/python
import turtle
def func_1(r):	
	c=range(r)
	a=['A' if i%2 == 0 else '' for i in range(r) ]
	b=['B' if i%3 == 0 else '' for i in range(r) ]
	
	for i in (zip(c,a,b)):	
		print i
r=10
def func_word(data):
	arr = data.split(' ')
	kol=len(arr)
	dct={}
	for item in arr:
		if item in dct:		
		   	dct[item] += 1
		else:
			dct[item] = 1
	
	col=len(dct)
	turtle.fd(50)
	turtle.dot(100, "yellow")
	
	for k, v in dct.iteritems():				
		u=360/kol
		turtle.forward(50)
		turtle.right(180)
		turtle.forward(50)
		turtle.right(u*v)	
	raw_input('q')
func_word("Line abcdef abc Line abcd hhhd")
	
