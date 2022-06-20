class circle():
	r=0
	def val(self):
		self.r=int(input("Enter the radius:"))
	def area(self):
		a=(self.r**2)*3.14
		print(a)
	def peri(self):
		p=2*3.14*self.r
		print(p)

r=circle()
r.val()
r.area()
r.peri()
