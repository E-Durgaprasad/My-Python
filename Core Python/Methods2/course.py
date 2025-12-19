"""Q5. Create a class Course that:
*Tracks total courses created.
*Each course has a title, duration, and enrolled_students.
*Provides a method to enroll a new student.
*Allows updating the minimum duration for a valid course across all instances.
*Has a static function to check if a given duration is realistic (not negative, not too large).
Demonstrate:
1.Creating multiple courses.
2.Enrolling students.
3.Updating minimum duration and checking durations."""

class Course:
    total_course=0
    min_duration=5


    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.enrolled_student=[]
        Course.total_course+=1

    def enroll_student(self,student_name):
        self.enrolled_student=student_name

    @classmethod
    def update_min_duration(cls,new_duration):
        cls.min_duration=new_duration


    @staticmethod
    def duration_time(duration):
        if duration>0:
            return "Invalid duration"

        elif duration>12:
            return "too long"
        elif duration < course.min_duration:
            return "Too short"
        else:
            return "Valid duration"


s1=Course(title="python",duration=2)
s2=Course(title="java",duration=5)

print(s1.duration_time(s1.duration))
print(s2.duration_time(s2.duration))
print(s3.duration_time(s3.duration))
Course.update_min_duration=10
print(s1.duration_time(s1.duration))
