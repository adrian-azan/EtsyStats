import student as st
import lesson as les

_DATE = 0
_LENGTH = 1
_NAME = 4
_SUBJECT = 5
_RATE = 7
_EARNED = 9


class tutor:

    def __init__(self):
        self.students = list()
        self.lesson = dict()

    def printLessons(self):
        for key in self.lesson:
            print(key)
            for lesson in self.lesson[key]:
                print(lesson.earned)
            print()

    def addLesson(self, student,details):
        newLesson = les.lesson()
        newLesson.setDate(details[_DATE])
        newLesson.setLength(details[_LENGTH])
        newLesson.setSubject(details[_SUBJECT])
        newLesson.setRate(details[_RATE])
        newLesson.setEarned(details[_EARNED])
        
        try:                        
            self.lesson[student.name].append(newLesson)
        except KeyError:
            self.lesson[student.name] = list()
            self.lesson[student.name].append(newLesson)

    def addStudent(self, name, subject):
        try:
            index = str(name).find(".")
            name = name[:index]
            student = st.student(name,subject)
            found = student in self.students
            if not found:
                self.students.append(student)
            return student
            
        except Exception:
            print(Exception)
            return None