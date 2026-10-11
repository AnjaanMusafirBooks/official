from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_report_summary_and_csv_use_same_filter_builder():
    src = (ROOT / "admin-dashboard.js").read_text()
    assert 'function reportQuery()' in src
    assert 'api("/api/v2/admin/reports/summary"+(q.toString()?' in src
    assert 'api("/api/v2/admin/reports/orders.csv"+(q.toString()?' in src
    for field in ['from:"date-from"','to:"date-to"','status:"report-status"','product_id:"report-product-id"','coupon:"report-coupon"','min_amount:"report-min-amount"','max_amount:"report-max-amount"']:
        assert field in src

def test_checkout_configuration_stays_staging_safe():
    config = (ROOT / "new-version-config.js").read_text()
    assert 'CHECKOUT_WORKER_URL: ""' in config
    assert 'CASHFREE_MODE: "sandbox"' in config
