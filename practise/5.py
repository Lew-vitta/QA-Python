def compare(first,second):
    for i in range(0, len(first)):     
        yeet = first[:i] + '' + first[i+1:]
        if  yeet == second:
            return(True)
    return(False)

print(compare("reset", "rest"))



def grade_calculator(input):
        total_score = 0
        for i in range(1,4):
            total_score += input[i]
        input.append(total_score)
        input.append((total_score/175)*100)
        if input[5] >= 70:
            input.append("A")
        elif input[5] >= 60:
            input.append("B")
        elif input[5] >= 50:
            input.append("C")
        elif input[5] >= 40:
            input.append("D")
        else:
            input.append("FAIL")

        return(input)

while 1:
    student=[]
    students=[]

    student.append(str(input("What is your name? ")))
    if student[0]=="done":
        break

    student.append(float(input("What is your Homework score? (/25) ")))
    student.append(float(input("What is your Assesment score? (/50) ")))
    student.append(float(input("What is your Exam score? (/100) ")))


    students.extend(grade_calculator(student))

print(students)




#def add_calc(number1, number2):
#    answer = number1 + number2
#    return answer


#added_number = add_calc(5,5)
#print(added_number + 20)