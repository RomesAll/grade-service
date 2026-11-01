from pathlib import Path
import pandas as pd


class OdfDataReader:
    """Чтение ODS-файла с баллами студентов."""
    ENGINE = 'odf'
    DTYPE = str

    def read(self, filepath: str) -> pd.DataFrame:
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Файл {path} не найден")

        df = pd.read_excel(path, engine=self.ENGINE, dtype=self.DTYPE)
        df.columns = [str(c).strip() for c in df.columns]
        return df
