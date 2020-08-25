if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_marks = student_marks[query_name]
    t = student_marks[0]+student_marks[1]+student_marks[2]
    print('{0:.{1}f}'.format(t/3, 2))
