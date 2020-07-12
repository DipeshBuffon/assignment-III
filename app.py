#Asking for query
query= input("Enter Q/q for query of course and E/e  to exit:- ")
if query.lower() == 'q':
    file = open('course.txt','r')
    print(file.read())
    file.close()

elif query.lower()=='e':
    print("Successfully exited!!!")
else:
    print("Invalid input")

#Admitting students function
students=[]
def admission():
    name = input('Enter your name:- ')
    print("You have to pay rs. 20,000 as depsout to get into course.")
    amount=int(input("Enter the amount you will pay:- "))
    calculate(name,amount)

def calculate(n,a):
    if a<10000 or a>20000:
        print("Amount is less than expected! and run program again")

    else:
        print("Congrats!!!You have been admitted successfully")
        remaining=20000-a
        file=open('student.txt','w')
        file.write("Name:- {}, Paid:- rs.{}, Left to be paid:- rs.{}".format(n,a,remaining))




#Asking for admission
a = input("Do you want admission? Press Y for yes and N for no:- ")

while a.lower() == 'y':
    admission()
    a=input("Do you want admission? Press Y for yes and N for no:- ")
