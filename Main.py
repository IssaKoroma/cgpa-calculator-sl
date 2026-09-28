# SIERRA LEONE UNIVERSAL CGPA CALCULATOR
# Supports Letter Grades: A, B+, B, B-, C+, C, C-, D, F

def get_point(grade, scale):
    grade = grade.upper().strip()
    # 4.0 Scale (USL, IPAM, IMATT, FBC, UNIMAK)
    map_4 = {
        "A": 4.0, "B+": 3.5, "B": 3.0, "B-": 2.5,
        "C+": 2.0, "C": 1.5, "C-": 1.0, "D": 0.5, "F": 0.0
    }
    # 5.0 Scale (MMTU, EBK, Eastern Tech, NCTVA)
    map_5 = {
        "A": 5.0, "B+": 4.5, "B": 4.0, "B-": 3.5,
        "C+": 3.0, "C": 2.5, "C-": 2.0, "D": 1.0, "F": 0.0
    }
    m = map_4 if scale == "1" else map_5
    return m.get(grade, None)

print("==================================================")
print("  SIERRA LEONE UNIVERSAL CGPA CALCULATOR")
print("==================================================")

name = input("Student Name: ")
sid = input("Student ID: ")
uni = input("University Name (e.g. IMATT, IPAM, MMTU): ")

print("\nSelect Grading Scale:")
print("1 = 4.0 Scale (USL, IPAM, IMATT, FBC, UNIMAK)")
print("2 = 5.0 Scale (MMTU, EBK, Eastern Tech, NCTVA)")
scale = input("Enter 1 or 2: ")
while scale not in ["1","2"]:
    print("Invalid! Enter 1 or 2")
    scale = input("Enter 1 or 2: ")

max_scale = "4.0" if scale=="1" else "5.0"
num = int(input(f"\nHow many modules: "))

total = 0
valid_count = 0
i = 1
while i <= num:
    g = input(f"Module {i} Grade: ")
    point = get_point(g, scale)
    if point is None:
        print("  Invalid grade! Use A, B+, B, B-, C+, C, C-, D, F")
        continue
    print(f"  -> {g.upper()} = {point}")
    total += point
    valid_count += 1
    i += 1

cgpa = total / valid_count if valid_count>0 else 0

# Class
if scale=="1":
    if cgpa>=3.6: cls="First Class"
    elif cgpa>=3.0: cls="Second Class Upper (2:1)"
    elif cgpa>=2.5: cls="Second Class Lower (2:2)"
    elif cgpa>=2.0: cls="Third Class"
    elif cgpa>=1.0: cls="Pass"
    else: cls="Fail"
else:
    if cgpa>=4.5: cls="First Class"
    elif cgpa>=3.5: cls="Second Class Upper"
    elif cgpa>=2.5: cls="Second Class Lower"
    elif cgpa>=1.5: cls="Third Class"
    else: cls="Fail"

print("\n========== RESULT ==========")
print(f"Name: {name} | ID: {sid}")
print(f"University: {uni} | Scale: {max_scale}")
print(f"CGPA: {cgpa:.2f} / {max_scale}")
print(f"Class: {cls}")
print("=============================")
