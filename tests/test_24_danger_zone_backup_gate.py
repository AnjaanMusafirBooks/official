from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_retention_cleanup_ui_requires_backup_first_guidance():
    js = (ROOT / "admin-dashboard.js").read_text()
    assert "पिछले 30 मिनट में encrypted backup export करें" in js
    assert 'DELETE EXPIRED TECHNICAL LOGS' in js
