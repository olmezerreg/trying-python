#!/usr/bin/python
#Filename; alhsab

#======================================================================================================#
  

#the arai of rect                                                                                      
def area_rect():
	lenght=int(input("plaes enter your lenght : "));
	wight =int(input("plaes enter your wight  : "));
	area  = wight * lenght;
	print ("the area  is ", area) ;	
area_rect()



#the arai of square
def area_square():
 side=int(input("plaes enter your side : "));
 area=side**2
 print ("the area  is ", area );
	
area_square()

#the arai of cercle
def area_cercle():
 radius=int(input("plaes enter your radius : "));
 area=(radius**2)*3.14
 print ("the area  is ", area );

area_cercle()


#the arai of triangle
                                                                                      
def area_triangle():
	base=int(input("plaes enter your base : "));
	height =int(input("plaes enter your height  : "));
	area  = (base * height)/2
	print ("the area  is ", area );	
area_triangle()

#the arai of trapeze
                                                                                      
def area_trapeze():
	small_base=int(input("plaes enter your small base : "));
	big_base =int(input("plaes enter your big base  : "));
	height =int(input("plaes enter your height  : "));
	area  = ((big_base + small_base)*height)/2
	print ("the area  is ", area );	
area_trapeze()
#======================================================================================================#
#surraindings of rect
def surraindings_rect():
	lenght= int(input ("  pleas enter your lenght :   "))
	whath=int(input("    pleas enter your whath :   "))
	surraindings=2*(whath+lenght)
	print("the surraindings is   ", surraindings) 
surraindings_rect()


#surraindings of square
def surraindings_square():
	side= int(input ("  pleas enter your side :   "))
	surraindings=side*4
	print("the surraindings is   ", surraindings) 
surraindings_square()


#surraindings of triangle
def surraindings_triangle():
	side1= int(input ("  pleas enter your side1 :   "))
	side2= int(input ("  pleas enter your side2 :   "))
	side3= int(input ("  pleas enter your side3 :   "))
	surraindings=side1+side2+side3
	print("the surraindings is   ", surraindings) 
surraindings_triangle()


#surraindings of trapeze
def surraindings_trapeze():
	side1= int(input ("  pleas enter your side1 :   "))
	side2= int(input ("  pleas enter your side2 :   "))
	side3= int(input ("  pleas enter your side3 :   "))
	side4= int(input ("  pleas enter your side4 :   "))
	surraindings=side1+side2+side3
	print("the surraindings is   ", surraindings) 
surraindings_trapeze()


#surraindings of cercle
def surraindings_cercle():
	radius= int(input ("  pleas enter your radius :   "))
	surraindings=radius*3.14
	print("the surraindings is   ", surraindings) 
surraindings_cercle()
#======================================================================================================#