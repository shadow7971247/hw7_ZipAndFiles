import os
import zipfile
import pytest


@pytest.fixture
def zip_archive():
    """Создаёт архив из файлов в папке tmp, пропускает тесты, если файлов нет."""
    test_dir = os.path.dirname(__file__)
    tmp_dir = os.path.join(test_dir, "tmp")

    pdf_file = os.path.join(tmp_dir, "document.pdf")
    xlsx_file = os.path.join(tmp_dir, "table.xlsx")
    csv_file = os.path.join(tmp_dir, "data.csv")

    missing = [f for f in [pdf_file, xlsx_file, csv_file] if not os.path.exists(f)]
    if missing:
        pytest.skip(f"В папке tmp нет файлов: {missing}")

    archive_path = os.path.join(test_dir, "test_files.zip")
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(pdf_file, arcname="document.pdf")
        zipf.write(xlsx_file, arcname="table.xlsx")
        zipf.write(csv_file, arcname="data.csv")

    yield archive_path

    if os.path.exists(archive_path):
        os.remove(archive_path)