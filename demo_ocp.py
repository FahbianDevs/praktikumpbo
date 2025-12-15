# demo_ocp.py
from models import Student, Course, RegistrationRequest
from validators import CreditValidator, PrerequisiteValidator, ActiveStatusValidator, ScheduleConflictValidator
from manager import ValidatorManager

def run_ocp_demo():
    student = Student(id="S002", current_sks=12, max_sks=24, is_active=True)
    # tambahkan time_slots pada Course untuk demo
    course = Course(code="CS301", sks=3, prerequisites=[])
    course.time_slots = ["Mon 09-11"]

    # jadwal existing: ada mata kuliah lain yang bentrok
    existing_schedule = {
        "CS201": ["Mon 09-11"],
        "MATH201": ["Tue 10-12"]
    }

    request = RegistrationRequest(student=student, course=course, completed_courses=[])

    validators = [
        CreditValidator(),
        PrerequisiteValidator(),
        ActiveStatusValidator(),
        ScheduleConflictValidator(existing_schedule)  # ditambahkan tanpa mengubah manager
    ]

    manager = ValidatorManager(validators)
    ok, messages = manager.validate_all(request)
    print("Hasil validasi (OCP demo):", ok)
    print("Messages:", messages)

if __name__ == "__main__":
    run_ocp_demo()
