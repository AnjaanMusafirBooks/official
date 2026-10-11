from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_orders_view_has_advanced_filter_controls():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    for field in ["orders-q", "orders-status", "orders-product-id", "orders-coupon", "orders-from", "orders-to", "orders-min-amount", "orders-max-amount", "orders-problems-only"]:
        assert f'id="{field}"' in html
    assert 'q.set("problem_only","true")' in js
    assert 'target==="orders-data"' in js
    assert "Abandoned checkout is not inferred" not in js
