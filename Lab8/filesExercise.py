# Sibtain Ahmed
# Oct 25, 2025

def readFile(file_name):   
    content = []
    with open(file_name, 'r', encoding='utf-8') as file:
        # content.append(file.readline().split(','))
        file.readline() 
        for line in file:
            content.append(line.split(','))
    return content

def studentScoreMapping(student_details, student_scores):
    student_to_scores = {}
    for id, name in student_details:
        student_to_scores[id.strip()] = [name.strip(), 0, 0]
    for id, _, score in student_scores:
        id = id.strip()
        score = int(score.strip())
        if id in student_to_scores:
            student_to_scores[id][1] += 1  
            student_to_scores[id][2] += score 
    return student_to_scores


def saveMappingToFile(mapping, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Student ID,Name,Total Scores,Sum of All Scores,Score Average")
        for student_id, values in mapping.items():
            file.write(f"\n{student_id},{values[0]},{values[1]},{values[2]},{values[1]/values[2]}")


def main():
    # student_file_name = input("Enter student details file name: ")
    student_details = readFile('students.txt')
    # score_file_name = input("Enter student scores file name: ")
    student_scores = readFile('scores.txt')
    student_to_scores = studentScoreMapping(student_details, student_scores)
    saveMappingToFile(student_to_scores, 'grades.txt')

if __name__ == "__main__":
    main()