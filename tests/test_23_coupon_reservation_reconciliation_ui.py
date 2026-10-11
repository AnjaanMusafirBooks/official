from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_coupon_admin_has_manual_safe_reconciliation_control():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'id="reconcile-coupon-reservations"' in html
    assert 'id="coupon-reconcile-status"' in html
    assert "Cashfree" in html and "Pending" in html
    assert "/api/v2/admin/coupons/reconcile-reservations" in js
    assert 'addEventListener("click",reconcileCouponReservations)' in js
