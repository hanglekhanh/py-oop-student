from meeting import meeting


class class_student(meeting):
    # course       : course of this class (course.py)
    # teacher      : who teach this class (teacher.py)
    # list_student : list student join this class (student.py)
    # start_time   : start time of this class
    # end_time     : end time of this class
    # id_meeting   : id of meeting or class
    def __init__(self, course, teacher, list_student, start_time, end_time, id_meeting):
        self.course = course
        self.teacher = teacher
        self.list_student = list_student
        meeting.__init__(self, start_time=start_time,
                         end_time=end_time, id_meeting=id_meeting)
