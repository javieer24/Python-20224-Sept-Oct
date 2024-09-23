def calculate_average(grades):
total = 0
for grade in grades:
total += grade
average = total / len(grades)
return average

grades_list = [85, 90, 78, 92, 88]
print(f"El promedio es: {calculate_average(grades_list)}")
