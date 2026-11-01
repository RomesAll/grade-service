from dataclasses import dataclass


@dataclass(frozen=True)
class GradeScale:
    """Доменная модель для хранения шкалы перевода баллов в оценку."""
    thresholds: tuple[tuple] = ((85.0, 5), (70.0, 4), (50.0, 3))
    default_grade: int = 2

    def grade(self, total_score: float) -> int:
        for threshold, grade in self.thresholds:
            if total_score >= threshold:
                return grade
        return self.default_grade