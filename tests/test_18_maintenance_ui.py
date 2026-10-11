from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_admin_maintenance_ui_wires_encrypted_export_and_restore():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'data-view="maintenance"' in html
    assert 'id="export-backup"' in html
    assert 'id="restore-backup-form"' in html
    assert '/api/v2/admin/maintenance/backup/export' in js
    assert '/api/v2/admin/maintenance/backup/restore' in js
    assert 'RESTORE STAGING DATABASE' in js


def test_backup_ui_warns_about_r2_and_staging():
    html = (ROOT / "admin-dashboard.html").read_text()
    assert "R2 में रखी PDF files इस backup में शामिल नहीं हैं" in html
    assert "APP_ENV=staging" in html
    assert "BACKUP_ENCRYPTION_KEY" in html
