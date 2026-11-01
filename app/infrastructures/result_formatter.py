from typing import Sequence
from app.domain import Student


class ConsoleResultFormatter:
    """Форматирует таблицу для вывода в консоль."""

    HEADER = f"{'ФИО':<40} | {'Сумма баллов':<15} | {'Оценка'}"
    SEPARATOR = "-" * 75

    def format(self, students: Sequence[Student]) -> str:
        lines = [self.HEADER, self.SEPARATOR]
        for s in students:
            lines.append(f"{s.name:<40} | {s.total_score:<15.1f} | {s.grade}")
        return "\n".join(lines)