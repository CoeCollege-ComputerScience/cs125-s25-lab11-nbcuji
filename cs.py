def finddoublemajors():
    with open("cs.txt", "r") as f1, open("math.txt", "r") as f2:
        cs_students = set(line.strip() for line in f1)
        math_students = set(line.strip() for line in f2)
    
    doublemajors = cs_students.intersection(math_students)
    return list(doublemajors)

print("\n".join(finddoublemajors()))

