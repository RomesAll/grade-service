import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence
import pandas as pd
import logging
from app.application import GradeUseCase
from app.domain import ScoreCalculator, GradeScale
from app.infrastructures import OdfDataReader, ConsoleResultFormatter

logger = logging.getLogger()


def main(argv: Sequence[str]) -> int:
    logger.info('Начало работы программы')
    if len(argv) < 2:
        logger.warning('Файл для обработки не был передан')
        return 1

    try:
        use_case = GradeUseCase(
            reader=OdfDataReader(),
            calculator=ScoreCalculator(),
            scale=GradeScale(),
            formatter=ConsoleResultFormatter(),
        )
        output = use_case.execute(argv[1])
    except FileNotFoundError as e:
        logger.error("Ошибка: %s", e)
        return 2
    except Exception as e:
        logger.error("Ошибка при чтении файла: %s", e)
        return 3

    print(output)
    return 0
