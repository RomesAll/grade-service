from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    """Доменная модель для хранения кол-ва балов и оценки."""
    name: str
    total_score: float
    grade: int