def sort_ax2_bx_c_given_sorted_x(x,a,b,c):
    """
    Goal: Given sorted list x, output sorted of F:=a*x**2+b*x+c
    
    """
    func = lambda x: a*x**2+b*x+1 
    arg_min_max=-b/(2.*a)  #2*a*x+b=0, x =-b/2a if a>0 it is min else max
    list1=[i for i in x if i<=arg_min_max] #Functions has symetry w.r.t to arg_min_max
    list2=[i for i in x if i>arg_min_max] # F(List1) is decreasing in a>0
    flist1=map(func,list1)
    flist2=map(func,list2)
    result=[]; 
    if a==0:
       if b<0:
        result=map(func,x);
        result.reverse()
       elif b>0:
        result=map(func,x); 
    elif a>0:
        flist1.reverse() #a>0  F(List1) is decreasing  so reverse it 
    elif a<0:
        flist2.reverse() #a  F(List2) is decreasing  so reverse it 

    while len(flist1)>0 and len(flist2)>0 :
        if flist1[0]>flist2[0]:
           result.append(flist2[0])
           flist2.pop(0)
        else:
          result.append(flist1[0])
          flist1.pop(0)  
    if flist1:
        [result.append(i) for i in flist1]
    if flist2:
        [result.append(i) for i in flist2]  
              
    return result

def is_sorted(lst):
        return lst == sorted(lst)           
     

#Checking the code for a>0
a=20
b=0
c=1
import numpy as np
x=[-2,-1,0,1,2]
Fx=sort_ax2_bx_c_given_sorted_x(x,a,b,c)
print Fx
print is_sorted(Fx)         

#Checking the code for a>0
a=-40
b=2
c=1
x=sorted(np.random.randn(100))
Fx=sort_ax2_bx_c_given_sorted_x(x,a,b,c)

print is_sorted(Fx)
