

def function():
           
           zeus = int(input("Ramdeni cifris shetana gindat: "))
           summ = 0

           for i in range(zeus):
                      n = int(input("Number here : "))
                      summ+=n
           
           return print("Your Middle Divedier is :",int(summ / zeus))


def fact():
           import math
           n  = int(input("Write number to get Factorial"))
           return print("Your factorial is",math.factorial(n))
           
while True :
           
           print(" 1 = Factorialis gamotvla || 2 = Sashvalo aritmetikulis gamoTva ")
           qeustion = int(input("airchiet romeli operacia gsurt "))


           if qeustion !=1 and qeustion !=2:
                      print("Choose only 1 || 2 ")
           elif qeustion == 1 :
                      fact()
           elif qeustion == 2 :
                      function()
           else:
                      print("Some Error Here " )


