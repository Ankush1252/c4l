from collections import defaultdict

def map_function(student_scores):
    """Emits tuples of student_id and score."""
    for student_id, score in student_scores:
        yield student_id, score
        
def reduce_function(mapped_data):
    """Assigns grades based on scores."""
    grades = {}
    for student_id, score in mapped_data:
        if score > 80:
            grade = 'A'
        elif score > 60:
            grade = 'B'
        elif score > 40:
            grade = 'C'
        else:
            grade = 'D'
        grades[student_id] = grade
    return grades

def map_reduce(student_scores):
    """Simulates the MapReduce process for assigning grades to students based on scores."""
    # Map phase
    mapped_data = list(map_function(student_scores))
    # Reduce phase
    grades = reduce_function(mapped_data)
    return grades  

# Example student scores (student_id, score)
student_scores = [
(1, 85),
(2, 75),
(3, 55),
(4, 35),
(5, 90)
]

# Find grades for students
grades = map_reduce(student_scores)

# Print grades for each student
for student_id, grade in grades.items():
    print(f"Student {student_id} has been assigned grade {grade}.")

