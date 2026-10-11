from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_reports_filters_are_present_and_shared_with_csv_export():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    for element_id in ["report-q", "report-status", "report-product-id", "report-coupon", "report-min-amount", "report-max-amount"]:
        assert f'id="{element_id}"' in html
    assert "function reportQuery()" in js
    assert 'const q=reportQuery();' in js
    assert 'anjaan-musafir-filtered-orders-report.csv' in js


def test_reports_explain_filtered_export():
    html = (ROOT / "admin-dashboard.html").read_text()
    assert "Download filtered CSV" in html
