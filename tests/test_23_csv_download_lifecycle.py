from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_csv_download_url_is_not_revoked_immediately():
    src = (ROOT / "admin-dashboard.js").read_text()
    assert 'setTimeout(()=>URL.revokeObjectURL(url),1000)' in src
    assert 'a.download="anjaan-musafir-filtered-orders-report.csv"' in src
