students = ["Hermine", "Harry", "Ron"]

#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]       #listcomprehension

gryffindors = {student: "Gryffindor" for student in students}      #dictcomprehension


"""
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
"""
print(gryffindors)