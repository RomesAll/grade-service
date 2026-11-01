from typing import Sequence
import pandas as pd
import logging
from app.domain.grade_scale import GradeScale
from app.domain.score_calculator import ScoreCalculator
from app.domain.student import Student
from app.infrastructures import OdfDataReader, ConsoleResultFormatter

logger = logging.getLogger()


class GradeUseCase:
    """Сценарий для определения оценки студентов по баллам."""

    def __init__(
        self,
        reader: OdfDataReader,
        calculator: ScoreCalculator,
        scale: GradeScale,
        formatter: ConsoleResultFormatter,
    ):
        self._reader = reader
        self._calculator = calculator
        self._scale = scale
        self._formatter = formatter

    def execute(self, filepath: str) -> str:
        # Чтение из файла
        logger.info('Начало чтения файла: %s ....', filepath)
        df = self._reader.read(filepath)
        logger.info('Файл %s успешно прочитан, начало обработки данных студентов ....', filepath)
        columns = [c for c in df.columns if "Задание" in c or "Тест" in c]

        # Подсчет баллов и определение оценки
        students: list[Student] = []
        for _, row in df.iterrows():
            name = str(row.iloc[0]).strip()
            if not name or name == 'nan':
                continue
            # Получение кол-ва баллов
            total = self._calculator.calculate(row, columns)
            # Определение оценки
            grade = self._scale.grade(total)

            # Сохранение результата обработки в список
            logger.debug('Студент %s, кол-во баллов (оценка): %s (%s)', name, total, grade)
            students.append(Student(name, total, grade))

        logger.info('Информация о студентах успешно обработана')
        # Форматирование выходных данных
        return self._formatter.format(students)