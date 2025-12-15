# manager.py
from typing import List, Tuple
from validators import Validator
from models import RegistrationRequest

class ValidatorManager:
    def __init__(self, validators: List[Validator]):
        """
        ValidatorManager bergantung pada abstraksi Validator (DIP).
        Untuk menambah aturan baru, cukup tambahkan instance Validator baru ke daftar.
        """
        self.validators = validators

    def validate_all(self, request: RegistrationRequest) -> Tuple[bool, List[str]]:
        """
        Jalankan semua validator. Kembalikan (is_all_valid, messages)
        Manager tidak perlu tahu detail tiap validator (OCP).
        """
        messages = []
        for v in self.validators:
            ok, msg = v.validate(request)
            messages.append(msg)
            if not ok:
                return False, messages
        return True, messages


# tambahan di validators.py atau file baru
class ScheduleConflictValidator(Validator):
    def __init__(self, existing_schedule):
        """
        existing_schedule: dict mapping course_code -> list of time slots (contoh sederhana)
        time slot bisa berupa string 'Mon 09-11' dsb.
        """
        self.existing_schedule = existing_schedule

    def validate(self, request: RegistrationRequest):
        # contoh sederhana: course.code punya slot 'Mon 09-11' dan jika ada overlap -> gagal
        # untuk demo, kita asumsikan course memiliki attribute 'time_slots' (list of str)
        course_slots = getattr(request.course, "time_slots", [])
        for slot in course_slots:
            for other_course, slots in self.existing_schedule.items():
                if slot in slots:
                    return False, f"Konflik jadwal dengan {other_course} pada {slot}"
        return True, "Tidak ada konflik jadwal"
