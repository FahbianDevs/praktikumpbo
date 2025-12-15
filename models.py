# models.py
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    id: str
    current_sks: int
    max_sks: int
    is_active: bool

@dataclass
class Course:
    code: str
    sks: int
    prerequisites: List[str]

@dataclass
class RegistrationRequest:
    student: Student
    course: Course
    completed_courses: List[str]
