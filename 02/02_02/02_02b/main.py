''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_books_list = [5, 3, 0, 7, 2, 4, 6, 8, 1, 3, 9, 5, 2, 6, 7, 4]

# First student read 3 more books
# Second student read 1 more book
# Last student read 2 more books

student_books_list[0] = student_books_list[0] + 3
student_books_list[1] += 1
student_books_list[-1] += 2

student_books_list.append(3)
student_books_list.append(5)

num_of_students = len(student_books_list)
print(f"There are {num_of_students} students in the class")

# sum / num of students

item_at_index_3 = student_books_list[3]

# Index Error: list index out of range
# print(student_books_list[20])

item_three_from_back = student_books_list[-3]
print(item_three_from_back)

# total_books = 0
# for individual_books in student_books_list:
#   total_books += individual_books
# print(total_books)
total_books = sum(student_books_list)

average_books = total_books / num_of_students
print(f"The average number of read books per student is {average_books:.2f}")