from pathlib import Path


def test_app_entrypoint_exists() -> None:
    assert Path("app.py").exists()
