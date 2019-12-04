# **************************************************************************************
# Concept 4.0.6: #Nested IF Statement
# **************************************************************************************
# >>>
gpa_total = 3.5
student_name = "John"
Enrolled = "True"

if Enrolled == "True":
    if student_name == "John":
        if gpa_total >= 3.0:
            print("Ready for Graduation")
        else:
            print("Not Ready for graduation")
    else:
        print("Not John")
else:
    print("Not enrolled.")
