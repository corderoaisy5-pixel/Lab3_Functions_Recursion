# main.py
import grades

# Students Identity Configuration
LAST_NAME = "CORDERO"
STUDENT_ID = "TUPM-25-0354"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores (Using a List [] instead of a Set {})
scores = [
    SEED_DIGIT * 10, 
    ID_SUM % 100, 
    NAME_LENGTH * 7
]

# Ensure these function names match grades.py exactly
average = grades.compute_average(scores)
grade = grades.assign_grades(average)  # Added 's'
remark = grades.generate_remark(grade) # Removed 'ed'

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average, 2)}") # Added 2 for cleaner decimals
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)