from unittest.mock import MagicMock
import pandas as pd
from app.application import GradeUseCase
from app.domain import ScoreCalculator, GradeScale
from app.infrastructures import ConsoleResultFormatter


def test_use_case_with_fake_data():
    # Создать тестовый набор данных
    test_df = pd.DataFrame({
        "ФИО": ["Зайцева Варвара", "Лукьянов Семён"],
        "Задание:ПР": ["-", "-"],
        "Тест:Тест 1": ["6", "2"],
        "Тест:Тест 2": ["10", "-"]
    })

    # Замокать ридер
    mock_reader = MagicMock()
    mock_reader.read.return_value = test_df

    use_case = GradeUseCase(
        reader=mock_reader,
        calculator=ScoreCalculator(),
        scale=GradeScale(),
        formatter=ConsoleResultFormatter()
    )

    result = use_case.execute("any_path.ods")

    assert "Зайцева Варвара" in result
    assert "2.0" in result