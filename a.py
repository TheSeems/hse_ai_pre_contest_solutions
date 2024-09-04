import typing as tp
from collections import namedtuple

Submission = namedtuple('Submission', ['student', 'task_number', 'verdict'])
Result = namedtuple('Result', ['student', 'total_submissions', 'total_successes'])

if __name__ == "__main__":
    n = int(input())

    submissions: tp.List[Submission] = []
    for i in range(n):
        raw = input().strip().split(maxsplit=3)
        submissions.append(Submission(student=raw[0], task_number=int(raw[1]), verdict=raw[2]))

    if len(submissions) == 0:
        exit(0)

    submissions.sort(key=lambda submission: (submission.student, submission.task_number, submission.verdict))

    results: tp.List[Result] = []
    i = 0
    while i < len(submissions):
        student = submissions[i].student
        total_submissions = 0
        total_successes = 0

        while i < len(submissions) and submissions[i].student == student:
            task_number = submissions[i].task_number
            has_success = False

            while i < len(submissions) and submissions[i].task_number == task_number and submissions[i].student == student:
                total_submissions += 1
                if submissions[i].verdict == 'OK':
                    has_success = True
                i += 1
            
            if has_success:
                total_successes += 1

        results.append(Result(student, total_submissions, total_successes))

    for result in results:
        print(result.student, result.total_submissions, result.total_successes)
    