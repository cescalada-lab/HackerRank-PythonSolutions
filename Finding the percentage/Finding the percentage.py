# my original code was this one:

if __name__ == '__main__':
    import numpy as np
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(np.mean((student_marks[query_name]))))
    
# but hackerrank didn't accept any library to do the code in this exercise, so i made this:

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(sum((student_marks[query_name]))/len((student_marks[query_name]))))
