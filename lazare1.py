#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 8 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  

#1. შექმენი კლასი car გაუკეთე 2 დეფაულტ ატრიბუტი , დაუმატე 2 მეთოდი, str და len. ასევე დინამიურად 2 შენს მიერ მოფიქრებული ატრბუტი.
# საბოლოოდ გამოჰქონდეს შესაბამისი მესიჯი.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.color = "pink"
#         self.year = 2000
#     def __str__(self):
#         return f"Car brand: {self.brand}, model: {self.model}, color: {self.color}, year: {self.year}"
#     def __len__(self):
#         return 2025 - self.year
#     def show_everything(self):
#         return f"The car brand is {self.brand}, car model is {self.model}, color is {self.color}, and year it came out is {self.year}"
# my_car = Car("Toyota", "Corolla")
# print(my_car.show_everything())  
# print(my_car)  
# print(f"The cars age is: {len(my_car)} years.")  






#2. დააიმპორტე მათემატიკის მოდული და იპოვე პოლიმორფიულდ ფართობები შემდეგი ფიგურებისთვის: წრე, კვადრატი, მართკუთხედი.
#გამოიტანე ყველას ფართობი, შესაბამისი მესიჯებით.

# import math


# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def __str__(self):
#         return f"Circle with radius {self.radius} and area {self.area():.2f}"


# class Square():
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def __str__(self):
#         return f"Square with side {self.side} and area {self.area()}"


# class Rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def __str__(self):
#         return f"Rectangle with length {self.length} and width {self.width}, area {self.area()}"


# circle = Circle(5)
# square = Square(4)
# rectangle = Rectangle(6, 3)

# print('Circle area:', circle)
# print('Square area:', square)
# print('Rectangle area:', rectangle)

#3. შექმენ პერსონ აიდის კლასი, სადაც დაახასიათებ სახელით, ასაკით , სქესით და ინფო მეთოდის მეშვეობით გამოიტან მომხმარებელზე ინფოს.

# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def info(self):
#         return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# person1 = Person("გიორგი", 12, "კაცი")
# person2 = Person("ანა", 20, "ქალი")

# print(person1.info())
# print(person2.info())

#4. შექმენი მშობელი კლასი გუნდი და შვილობილლი ფეხბურთისგუნდი, შექმენით Team კლასი, რომელსაც აქვს ფეხბურთელების სია. შექმენით FootballTeam კლასი, რომელიც მემკვიდრეობას იღებს Team კლასიდან.
#შექმენით Team კლასი, რომელსაც აქვს ფეხბურთელების სია. შექმენით FootballTeam კლასი, რომელიც მემკვიდრეობას იღებს Team კლასიდან. გამოიყენე super() ფუნქციაც.
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:

# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players = []

#     def add_player(self, player_name):
#         self.players.append(player_name)

# class FootballTeam(Team):
#     def __init__(self, name, coach):
#         super().__init__(name)
#         self.coach = coach

#     def show_info(self):
#         print(f"Team: {self.name}, Coach: {self.coach}")
#         print("Players:", ', '.join(self.players))

# team = FootballTeam("FC Barcelona", "hanski flick")
# team.add_player("yamal")
# team.add_player("dani olmo")
# team.show_info()


#5. მოიფიქრე და შექმენი წიგნების მართვის სისტემა. (ყოველივე მოიფიქრე შენით, შეგიძლია გამოიყენო 2 კლასი/ნებისმიერი მეთოდებით.)
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
        
#     def show_smth(self):
#         print(f'Book name is {self.title} and book author is {self.author}')
     
# book = Book('Jinsebis Taoba', 'Davit Turashvili')
# book.show_smth()

# class Library:
#     def __init__(self, library_name):
#         self.library_name = library_name
    
#     def wch_libr(self):
#         print(f'You can find this book in {self.library_name}')

# okk = Library('Oxford Library')
# okk.wch_libr()

    


#6. მოხმარებელთა მართვის სისტემა: შექმენით User კლასი, რომელიც მოიცავს სახელს, ასაკს და ელ.ფოსტას. დაამატეთ Admin კლასი, რომელიც მემკვიდრეობს User კლასიდან და აქვს მეთოდად დამატებითი უფლებები.
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:
# class User:
#     def __init__(self, name, age, email):
#         self.name, self.age, self.email = name, age, email

#     def oooik(self):
#         print(f'{self.name}, {self.age}, {self.email}')


# class Admin(User):
#     def add_user(self, user_list, name, age, email):
#         user_list.append(User(name, age, email))

# users = []
# admin = Admin('elena', 23, 'elena@gmail.com')
# admin.oooik()



#7. შექმენი სოც.ქსელის პლატფორმის მართვის სისტემა: კლასი მომხმარებლით დაახასიათე მომხარებელი, და ერთი ატრიბუტი წარმოადგენდეს ლისტს:
# შემდეგნაირად:
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.friends = []
    
#     def add(self, friend):
#         self.friends.append(friend)
    
#     def show(self):
#         print([friend.name for friend in self.friends])


# user1 = User('გივი', 28)
# user2 = User('ჭიჭიკო', 25)

# user1.add(user2)
# user1.show()  



# შექმენი მეგობრის დამატების მეთოდი მოცემულ კლასსში. დაამატე კლასი SocialMediaUser. წამოიღე მომკვიდრეობითი ატრიბუტები და დაამატე ერთი ატრიბური. გამოიტანე შესაბამისი შედეგი.

#8. შექმენი ბანკის ანგრიშების მართვის სისტემბა:შექმენით BankAccount კლასი, რომელიც მოიცავს ანგარიშის ნომერს, ბალანსსა და დეპოზიტების/ამოღებების მეთოდებს. 
# ბალანსი უნდა იყოს private და უნდა შესაბამისი მეთოდებით უნდა შეგვეძლოს ანგარიშის გამოტანა, და მისი შეცვლა.
# class BankAccount:
#     def __init__(self, account_number):
    
#         self.__account_number = account_number  
        
#         self.__balance = 0  
    
#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"დეპოზიტი შესრულდა {amount} ზე. ახლანდელი ბალანსი: {self.__balance}")
#         else:
#             print("არასწორი თანხა, დეპოზიტი ვერ განხორციელდება.")
    
#     def efd(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print(f"ამოღება განხორციელდა {amount} ზე. ახლანდელი ბალანსი: {self.__balance}")
#         else:
#             print("არასწორი თანხა ან საკმარისი ბალანსი არ არის.")
    
#     def get_account_number(self):
#         return self.__account_number

# account = BankAccount("123456789")
# print(f"ანგარიშის ნომერი: {account.get_account_number()}")

# account.deposit(1200)
# account.efd(50)
# account.efd(60)

# print(f"ბალანსი საბოლოოდ: {account.get_balance()}")

#9. მოიფიქრე ოოპ-ის გამოყენების მაგალითი.

# class Car:
#     def __init__(self, brand):
#         self.brand = brand 
#     def show_brand(self): 
#         return f"The car brand is {self.brand}"
# my_car = Car("Toyota")
# print(my_car.show_brand()) 

#10. მოიფიქრე და დაახასიათე ნებისმიერი ობიექტი ოოპის მემკვიდრეობის მეშვოებით. გამოიყენე იერარქიული მემკვიდრეობა.

class Animal:
    def sound(self):
        print("[animal sounds]")
class Dog(Animal):
    def do_trick(self):
        print("The dog rolled over!")
class Cat(Animal):
    def do_not_do_that(self):
        print("The cat did it anyway :)")
dog = Dog()
dog.sound()
dog.do_trick()
cat = Cat()

cat.sound()
cat.do_not_do_that()