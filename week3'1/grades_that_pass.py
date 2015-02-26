def grades_that_pass(students,grades,limit):
    spisuk=[]
    for i in range (0, len(grades)):
        if grades[i]>=limit:
            spisuk=spisuk+[students[i]]
    return spisuk
