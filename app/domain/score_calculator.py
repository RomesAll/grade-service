from typing import Sequence
import pandas as pd


class ScoreCalculator:
    """Считает итоговый балл студента по набору колонок."""

    MAX_SCORE = 100.0
    TEST_THRESHOLD = 5.0
    EMPTY_MARKERS = ('nan', )

    def calculate(self, row: pd.Series, columns: Sequence[str]) -> float:
        total = 0.0
        for col in columns:
            raw = row[col]

            if pd.isna(raw):
                continue
            text = str(raw).strip()
            if text in self.EMPTY_MARKERS:
                continue

            try:
                value = float(text.replace(',', '.'))
            except ValueError:
                continue

            if "Тест" in col:
                total += 1.0 if value > self.TEST_THRESHOLD else 0.0
            else:
                total += value

        return min(total, self.MAX_SCORE)