class Rectangle:
	height=int(input("Enter the height of rectangle:"))
	width=int(input("Enter the width of rectangle:"))
	corner_x1=int(input("Enter the corner x1 of rectangle:"))
	corner_y1=int(input("Enter the corner y1 of rectangle:"))
	corner_x2=int(input("Enter the corner x2 of rectangle:"))
	corner_y2=int(input("Enter the corner y2 of rectangle:"))
	def center(self):
		x1=self.corner_x1
		y1=self.corner_y1
		x2=self.corner_x2
		y2=self.corner_y2
		x=(x1+x2)//2
		y=(y1+y2)//2
		print("center=",x,y)
	def area(self):
		a=self.height*self.width
		print("Area=",a)
	def per(self):
		p=2*(self.height+self.width)
		print("perimeter=",p)
rec=Rectangle()
rec.center()
rec.area()
rec.per()
