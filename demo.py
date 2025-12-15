# demo.py
from models import Student, Course, RegistrationRequest
from validators import CreditValidator, PrerequisiteValidator, ActiveStatusValidator
from manager import ValidatorManager

def run_demo():
    student = Student(id="S001", current_sks=18, max_sks=20, is_active=True)
    course = Course(code="CS201", sks=3, prerequisites=["MATH101"])
    request = RegistrationRequest(student=student, course=course, completed_courses=["MATH101"])

    # daftar validator awal
    validators = [
        CreditValidator(),
        PrerequisiteValidator(),
        ActiveStatusValidator()
    ]

    manager = ValidatorManager(validators)
    ok, messages = manager.validate_all(request)
    print("Hasil validasi:", ok)
    print("Messages:", messages)

if __name__ == "__main__":
    run_demo()
