students = [
    ("John", 17, 88),
    ("Alice", 16, 92),
    ("Bob", 18, 85),
    ("Sarah", 17, 96),
    ("Mike", 16, 79)
]

print("Initial list of students:")
for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")

classroom = {
    "students": students
}

print("\nClassroom dictionary created with students list")

print("\n--- Adding new student ---")
new_student = ("Emma", 17, 94)
classroom["students"].append(new_student)
print(f"Added: {new_student}")

print("\n--- Removing student by name ---")
student_to_remove = "Bob"

for i, student in enumerate(classroom["students"]):
    if student[0] == student_to_remove:
        removed_student = classroom["students"].pop(i)
        print(f"Removed: {removed_student}")
        break

print("\n--- Finding highest grade ---")
highest_grade = max(classroom["students"], key=lambda student: student[2])
print(f"Highest grade: {highest_grade[2]} (achieved by {highest_grade[0]})")

print("\n--- Sorting students by grade (descending) ---")
classroom["students"].sort(key=lambda student: student[2], reverse=True)

print("\n--- Final classroom dictionary ---")
print("Classroom contents:")
for i, student in enumerate(classroom["students"], 1):
    print(f"{i}. Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")

print(f"\nTotal students in classroom: {len(classroom['students'])}")
print(f"Average grade: {sum(student[2] for student in classroom['students']) / len(classroom['students']):.1f}")
