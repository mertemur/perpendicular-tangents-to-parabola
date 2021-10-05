import math


class Inside(Exception):
    pass
class On(Exception):
    pass


def convertFloat(inp):
    try:
        return float(inp)
    except ValueError:
        num, den = inp.split('/')
        try:
            whole, num = num.split(' ')
            whole = float(whole)
        except ValueError:
            whole = 0
        frac = float(num) / float(den)
        return whole - frac if whole < 0 else whole + frac
    except:
        print("Be careful about input!")

def checkThePoint():
    a = convertFloat(input("Factor of parabola's x^2 : "))
    if(a==0.0):
        print("It's not a parabola!!")
        exit()
    b = convertFloat(input("Factor of parabola's x : "))
    c = convertFloat(input("Constant of parabola : "))
    parabola = "y = "+str(a)+"x^2"+" +"+str(b)+"x"+" +"+str(c)
    print(parabola)
    d = convertFloat(input("Point's x value : "))
    e = convertFloat(input("Point's y value : "))
    point = "P("+str(d)+","+str(e)+")"
    print(point)

    try:
        if(a>0):
            if(e > a*(d**2)+b*d+c):
                raise Inside
            elif(e == a*(d**2)+b*d+c):
                raise On
        if(a<0):
            if(e < a*(d**2)+b*d+c):
                raise Inside
            elif(e == a*(d**2)+b*d+c):
                raise On

        if(b == math.sqrt(4*a*(c-e)-1)):
            print("Tangents drawn from ", point,"to ", parabola, "intersect perpendicularly.")
        elif(b == -math.sqrt(4*a*(c-e)-1)):
            print("Tangents drawn from ", point,"to ", parabola, "intersect perpendicularly.")
        else:
            print("Nope! Tangents aren't intersect perpendicularly!")
    except Inside:
        print("The point is IN the parabola. You can't draw any tangent.")
        pass
    except On:
        print("The point is ON the parabola. You can draw only one tangent.")
        pass
    except:
        print("Nope! Tangents aren't intersect perpendicularly!")

def findTheMissing():
    print("y = a.x^2 + b.x + c    P(d,e) \nType the value you want to find.")
    missing = input("a/b/c/e ?")
    try:   
        if(missing == "a"):
            b = convertFloat(input("b = "))
            c = convertFloat(input("c = "))
            e = convertFloat(input("e = "))
            a = ((b**2)+1)/(4*(c-e))
            print("a = ", a)
        elif(missing == "b"):
            a = convertFloat(input("a = "))
            c = convertFloat(input("c = "))
            e = convertFloat(input("e = "))
            b = math.sqrt(4*a*(c-e)-1)
            print("b = ",b," or ", -b)
        elif(missing == "c"):
            a = convertFloat(input("a = "))
            b = convertFloat(input("b = "))
            e = convertFloat(input("e = "))
            c = (((b**2)+1)/(4*a))+e
            print("c = ",c)
        elif(missing == "e"):
            a = convertFloat(input("a = "))
            b = convertFloat(input("b = "))
            c = convertFloat(input("c = "))
            e = c - (((b**2)+1)/(4*a))
            print("e = ",e)
    except:
        print("Can't be!")


print("1)Give parabola and point to check whether the tangents intersect perpendicularly or not.\n2)Give other parameters and find the not given one.")
mode = input("1/2 ? ")
if(mode == "1"):
    checkThePoint()
elif(mode == "2"):
    findTheMissing()