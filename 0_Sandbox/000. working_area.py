
# **************************************************************************************
# Concept 4.0.6: #Nested IF Statement
# **************************************************************************************
# >>>
gpa_total = 2.5
student_name = "John"
Enrolled = "False"

if Enrolled == "True":
    if student_name == "John":
        if gpa_total >= 3.0:
            print("CONGRATS John! You are ready to graduate")
        elif gpa_total >= 1.0:
            print("GPA in fail range. More courses needed. ")
        else:
            print("Sorry John! GPA too low for graduation.")
    else:
        print("HMMMMM :( Not John! Access not allowed.")
else:
    print("Hmmm : You are not currently enrolled. Talk to Admissions.")
