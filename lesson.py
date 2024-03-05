
#mylist  = [12, 45, 89, 90, 56]
# d=[]
# s=[]
# def find_number(*mylist):  ### args
#
#     for i in list(mylist):
#         if i%2==0:
#             s.append(i)
#
#         elif i%2==1:
#             d.append(i)
#
#     print("toq sonlar=",d)



### 10
# f=[12, 5, 3, 2]
# def count_sum(f):
#     s = f[0]
#
#     for i in f:
#         if s>i:
#            s=i
#     print(s)
#
#     for i in f:
#         a=s*i
#         print(a)
#
#
# print(count_sum(f))


# def loo(a, b):
#     if a>b:
#         return "A kotta"
#     elif b>a:
#         return "B kotta "
#     else:
#         return "teng "
#
# print(loo(a=int(input("A=")), b=int(input("B="))))

# def add(a, b):
#     c=a+b
#     return c
#
#
# def daraja(x, a, b):
#     c=add(a, b)
#     return c**x
#
#
# def next(a, b, x, y):
#     m=daraja(x, a, b)
#     return m*y
#
# print(next(1, 1, 2, 1))


# i=0
# while i<3:
#     print i
#     i +=1
#
# else:
#     print i
#

# n=int(input("A="))
# for i in range(2, int(n**0.5)+1):
#           if i%n==0:
#              break
#
# else:
#     print(True)

# class C:
#      a= lambda  self: self.b(2)
#      def __init__(self):
#          self.b= lambda x:print(x**2)
#
# c=C()
# print(type(c.b))
# print(type(c.a))

# my = [[1], [2, 3], [4, 5, 6]]
# d= sum(my, [])
# print(d)

# s=0
# def ls():
#     s +=1
#
# ls()
# def f():
#     return [lambda x:i*x for i in range(5)]
#
# for d in f():
#           print(d(2))

# i=0
# while i<3:
#      print (i)
#      i++
#      print (i+1)


# class Person:
#     def __init__(self, f, l):
#        self.f = f
#        self.l=l
#
#
# class S(Person):
#      def __init__(self, f, l):
#         super.__init__(f, l)
#
# v=C


####  work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list
# elementlariga ko'paytirib qiymatini o'zgartiradi va listni print qilsin.


# def digit_count_and_sum(word):
#        v=word[0]
#        #v=min(word)
#        for i in word:
#            if v>i:
#               v=i
#
#        for i in word:
#            s=i*v
#            print(s)
#
#
# digit_count_and_sum([12, 2, 4, 8])


# def big_sales(sales):
#     a= max(sales.values())
#     b=list(sales.keys())
#     for i in sales.items():
#         if i ==a:
#            print(i)
#
#
# sales = {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
# c = big_sales(sales)
# print("Eng ko'p sotilgan oy:", c)
#

# def big_sales(sales):
#     key=list(sales.values())
#     k=list()
#     x=max(key)
#
#     for i in sales:
#         if sales[i]==x:
#               print(i)
#
# sales={ "yanvar": 12000,
#         "mart": 6000,
#         "aprel": 15000,
#         "sentabr": 9000,
#         "dekabr": 10000}
#
#
# big_sales(sales)

# regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
#            ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
#
# def find_last_regions(regions):
#     end = regions[0][1]
#     for i in regions:
#         for region in regions:
#             if region[0] == end:
#                 end = region[1]
#     return end
# print(find_last_regions(regions))

#### 2chi yol yol xaritasi
#
# regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"], ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
# end = regions[0][1]
# for region in regions:
#     if region[1] not in [x[0] for x in regions]:
#         end = region[1]
#         break
# print(end)

#
# from datetime import datetime
#
#
# a=input("Ismiz kiriting=")
# b=int(input("Tugulgan yilingiz="))
# c=datetime.now()
# #v=int(c.strftime('%Y'))-b
# #print(v)
# print(c.strftime('%Y-%m-%d-%c'))
#


# import calendar
# b=calendar.month(2024, 2)
# print(b)



# from turtle import *
#
# def floo():
#     for i in range(300):
#         circle(190-i, 90)
#         left(90)
#         circle(190-i, 90)
#         left(18)
#
# floo()
# mainloop()


#from datetime import datetime
#b=datetime.now()
#print(b.strftime('%Y-%m-%d-%c'))

#
# class Traff:
#
#     def __init__(self, color):
#         self.color = color
#
#     def action(self):
#         if self.color=='red':
#             print('Stop & wait')
#         elif self.color=='yellow':
#             print('Prepare to stop')
#         elif self.color=='green':
#             print('Go')
#         else:
#             print('Stop drinking 😉')
#
# yellow = Traff('red')
# yellow.action()

###3 find_more_letter(word1, word2, letter) - bu
# funksiya qaysi so'zda (yani "word1" va "word2") ko'p "letter"
# ishlatilgan aniqlab shu so'zni return qiladi.


