#!/usr/bin/python
#Filename; alhsab

#======================================================================================================#
                                                                                                       
                                                                                                       
                                                                                                       
#the arai of rect                                                                                      
def area_rect():
	lenght=input("plaes enter your lenght : ");
	wight =input("plaes enter your wight  : ");
	area  = wight * lenght
	print "the area  is ",area ;	
area_rect()



#the arai of square
def area_square():
 side=input("plaes enter your side : ");
 area=side**2
 print "the area  is ",area ;
	
area_square()

#the arai of cercle
def area_cercle():
 radius=input("plaes enter your radius : ");
 area=(radius**2)*3.14
 print "the area  is ",area ;

area_cercle()


#the arai of triangle
                                                                                      
def area_triangle():
	base=input("plaes enter your base : ");
	height =input("plaes enter your height  : ");
	area  = (base * height)/2
	print "the area  is ",area ;	
area_triangle()

#the arai of trapeze
                                                                                      
def area_trapeze():
	small_base=input("plaes enter your small base : ");
	big_base =input("plaes enter your big base  : ");
	height =input("plaes enter your height  : ");
	area  = ((big_base + small_base)*height)/2
	print "the area  is ",area ;	
area_trapeze()




















