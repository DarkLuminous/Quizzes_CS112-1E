import os


#Quiz 2

def One():
 miLes = 100                 #Step 1: Use a variable named miles with initial value 100.
 kLm = miLes * 1.609         #Step 2: Multiply miles by 1.609 and assign it to a variable named kilometers.
 print(kLm,"kilometer")      #Step 3: Display the value of kilometers.

                             #Output: 160.9 kilometer
 input("Continue . . . ")
 os.system('cls')
 Two()

def Two():
 #How would you rewrite the expression if you wished the result to be an integer number? 
 print("25 / 4")
 
 #To obtain an integer result, i'll use the floor division operator //, which discards the decimal part of the division.
 Ans = 25 // 4               
 print("The Answer is:", (Ans))            



 input("Continue . . . ")
 os.system('cls')
 Three()
 
def Three():
 
 print("4/3(r+34) - 9(a+bc) + 3+d(2+a)/a+bd")

 _r = float(input("r:"))
 _a = float(input("a:"))
 _b = float(input("b:"))
 _c = float(input("c:"))
 _d = float(input("d:"))
 

 P_a1 = _r + 34                  #1st Polynomial
 P_b1 = 3 * P_a1
 P_1 = 4 / P_b1
 
 #print(P_1,"1st")
 
 P_a2 = _a + _b * _c              #2nd Polynomial
 P_2 = 9 * P_a2

 #print(P_2,"2nd")
 
 P_a3 = 2 + _a                   #3rd Polynomial
 P_b3 = P_a3 * _d
 P_3 = 3 + P_b3
 
 #print(P_3,"3rd")

 P_4 = _b * _d + _a              #4th Polynomial
 
 #print(P_4,"4th")
 
 P_34 = P_3 / P_4                #3rd and 4th combined
 
 
 Ans = P_1 - P_2 + P_34
 print("The Answer is:",round(Ans,2))

 
One()