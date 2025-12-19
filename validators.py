# validators.py
from abc import ABC, abstractmethod
from typing import Tuple
from models import RegistrationRequest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class Validator(ABC):
    """
    Abstract base class for validation rules.

    Methods:
        validate(request: RegistrationRequest) -> Tuple[bool, str]:
            Validate the given registration request.
    """
    @abstractmethod
    def validate(self, request: RegistrationRequest) -> Tuple[bool, str]:
        pass

class CreditValidator(Validator):
    """
    Validates whether the student exceeds the maximum allowed SKS.
    """
    def validate(self, request: RegistrationRequest):
        """
        Check if the student's current SKS plus the course SKS exceeds the maximum.

        Args:
            request (RegistrationRequest): The registration request to validate.

        Returns:
            Tuple[bool, str]: Validation result and message.
        """
        s = request.student
        c = request.course
        if s.current_sks + c.sks > s.max_sks:
            logging.warning(f"Melebihi SKS maksimum ({s.max_sks})")
            return False, f"Melebihi SKS maksimum ({s.max_sks})"
        logging.info("SKS OK")
        return True, "SKS OK"

class PrerequisiteValidator(Validator):
    """
    Validates whether the student has completed all prerequisites for the course.
    """
    def validate(self, request: RegistrationRequest):
        """
        Check if all prerequisites for the course are completed.

        Args:
            request (RegistrationRequest): The registration request to validate.

        Returns:
            Tuple[bool, str]: Validation result and message.
        """
        missing = [p for p in request.course.prerequisites if p not in request.completed_courses]
        if missing:
            logging.warning(f"Prasyarat belum terpenuhi: {', '.join(missing)}")
            return False, f"Prasyarat belum terpenuhi: {', '.join(missing)}"
        logging.info("Prasyarat OK")
        return True, "Prasyarat OK"

class ActiveStatusValidator(Validator):
    """
    Validates whether the student is currently active.
    """
    def validate(self, request: RegistrationRequest):
        """
        Check if the student is active.

        Args:
            request (RegistrationRequest): The registration request to validate.

        Returns:
            Tuple[bool, str]: Validation result and message.
        """
        if not request.student.is_active:
            logging.warning("Mahasiswa tidak aktif")
            return False, "Mahasiswa tidak aktif"
        logging.info("Status aktif OK")
        return True, "Status aktif OK"
