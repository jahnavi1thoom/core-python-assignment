# Input
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
def calculate_averages(students):
    averages = {}
    for student, scores in students.items():
        averages[student] = round(sum(scores) / len(scores), 2)
    return averages
def top_performer(averages):
    return max(averages, key=averages.get)
averages = calculate_averages(students)
top = top_performer(averages)
print("Average Marks:", averages)
print(f'Top Performer: "{top}"')
