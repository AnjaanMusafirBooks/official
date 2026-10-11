from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "admin-dashboard.html").read_text()
JS = (ROOT / "admin-dashboard.js").read_text()
def test_product_edit_archive_actions_are_wired():
    assert 'function editProduct(item)' in JS
    assert 'function archiveProduct(item)' in JS
    assert '"/archive"' in JS
    assert 'method:"PATCH"' in JS
def test_coupon_edit_and_active_toggle_are_wired():
    assert 'function editCoupon(item)' in JS
    assert 'function toggleCoupon(item)' in JS
    assert '"/api/v2/admin/coupons/"' in JS
def test_frontend_validation_matches_backend_limits():
    assert 'maxlength="120"' in HTML and 'name="slug"' in HTML
    assert 'minlength="3" maxlength="40"' in HTML
