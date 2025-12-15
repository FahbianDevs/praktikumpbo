# validators.py
from abc import ABC, abstractmethod
from typing import Tuple
from models import RegistrationRequest

class Validator(ABC):
    @abstractmethod
    def validate(self, request: RegistrationRequest) -> Tuple[bool, str]:
        """Return (is_valid, message)"""
        pass

class CreditValidator(Validator):
    def validate(self, request: RegistrationRequest):
        s = request.student
        c = request.course
        if s.current_sks + c.sks > s.max_sks:
            return False, f"Melebihi SKS maksimum ({s.max_sks})"
        return True, "SKS OK"

class PrerequisiteValidator(Validator):
    def validate(self, request: RegistrationRequest):
        missing = [p for p in request.course.prerequisites if p not in request.completed_courses]
        if missing:
            return False, f"Prasyarat belum terpenuhi: {', '.join(missing)}"
        return True, "Prasyarat OK"

class ActiveStatusValidator(Validator):
    def validate(self, request: RegistrationRequest):
        if not request.student.is_active:
            return False, "Mahasiswa tidak aktif"
        return True, "Status aktif OK"
