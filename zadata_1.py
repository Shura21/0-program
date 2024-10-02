grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = str({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
grades_1=[5, 3, 3, 5, 4]
grades_2=[2, 2, 2, 3]
grades_3=[4, 5, 5, 2]
grades_4=[4, 4, 3]
grades_5=[5, 5, 5, 4, 5]
ball=(sum(grades_1)/len(grades_1),
      sum(grades_2)/len(grades_2),
      sum(grades_3)/len(grades_3)
      ,sum(grades_4)/len(grades_4),
      sum(grades_5)/len(grades_5))
print(ball)
average_score={'Aaron':4.0,'bilbo':2.25,'Johnny':4.0,'Khendrik':3.6666666666666665,'Steve':4.8}
print(average_score)