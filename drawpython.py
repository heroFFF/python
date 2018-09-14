Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.setup(650,350,200,200)
>>> import turtle as t
>>> t.penup()
>>> t.fd(-250)
>>> t.pendown()
>>> t.pensize(26)
>>> t.pencolor("blue")
>>> t.seth(-40)
>>> for i in range(4):
	t.circle(40,80)
	t.circle(-40,80)

	
	
>>> t.circle(40,80/2)
>>> t.fd(40)
>>> t.circle(16,180)
>>> t.fd(40*2/3)
>>> t.pensize(0.6)
>>> t.pencolor("black")
>>> t.circle(2)
>>> t.done()
