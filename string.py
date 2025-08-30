# string duplication
x = 'beautiful'
x.upper()
x.lower()
x.capitalize()

poem ='''Johny johny yes papa
eating sugar no papa
telling a lie no papa
open your mouth hahaha'''
print(poem)


poem.find('papa')

p = poem.replace('papa','fufa').replace('sugar','poison')
print(p)

a ="You are fool"
a.split()


poem.splitlines()

path = ['C:', 'User','Desktop','python']
print('/'.join(path))


text ="I learning Python"
word = text.split()
word.insert(1, "am")
new_text = " .join(words)
print(new_text)




student ={"Awantika":"19","Shaili":"50","Sadhvi":"47"}
print(student)


temp ={
    'lko' [35,40,38],
    'delhi' [30,32,34],
    'mumbai' : [28,26,30]
}
print(temp)

info = dict(name = "Alice", age = input("Enter your age"), city ="lko")
print(info)

#1st method to access value through key
student['Shaili']
info['city']

#2nd method to access value through key
student.get("name")
temp.get("lko")

print(student.keys())
print(student.value())
print(student.items())

for k,v info.items():
    print(f'{k} : {v}')


company = {
    'emp001':{
        'name': 'Alice',
        'age': 30,
        'department': 'HR'
    },
    'emp002':{
        'name':'Bob',
        'age': 25,
        'department': 'IT'
    },
    'emp003':{
        'name':'Charlie',
        'age': 27,
        'department': 'Finance'
    }
}
print(company)

company['emp004'] ={
    'name': 'David',
    'age': 35,
    'department': 'Marketing'
}
print(company)



#print the average temperature of lko key of temp dictionary
print(sum(temp['lko'])/len(temp['lko']))

-user defined functions
parameterized functions
non parameterized functions
return functionnon return function
default parametterized function
lambda function

-built in function

#non parameterized function
def greet():#
    print("Hello user")
    print("Welcome to our function notebook")
    print("See You in another class")
    greet()#function calling

    greet()


    #parameterized function
    def sum(a+b):#parameters
        print(a+b)

        sum(10+20)

        def avg(a,b,c,d):
            avg= (a+b+c+d)/4
            print(avg)

            #default parameterized 
            def myCountry(country):
                print(f'I love{country}')
            myCountry("USA")
            myCountry("Canada")
            myCountry("UK")
            myCountry() 


            def square(a):
                return a**2
            square(5)

            square = lambda a : a**2 
            print(square(5))

            def even(a):
                return(a%2==0)
            even()

            def even(n):
                if n % 2 ==0:
                    print("even number")
                else:
                    print("odd number")
            even(5) 

            even = lambda n : print("even  number") if n%2==0 else print("odd number")
            even() 


        -to find the number is prime or not

        def prime (n):
            if n % 1 ==0
                print("prime number")
            else:
                print("is not prime")              
              

num = int(input("Enter a number"))
if num < 2:
    print("Not prime")
else:
    for i in range(2,num+1):
        if num%i==0:
            print("Not prime")
            break
        else:
            print("Prime")