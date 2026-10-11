from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "admin-dashboard.html").read_text()
js = (ROOT / "admin-dashboard.js").read_text()
css = (ROOT / "admin-dashboard.css").read_text()
def test_forms_exist():
    assert 'id="product-create-form"' in html
    assert 'id="coupon-create-form"' in html
def test_routes_match_worker():
    assert '"/api/v2/admin/products"' in js
    assert '"/api/v2/admin/coupons"' in js
def test_auth_token_sent():
    assert 'Authorization:"Bearer "+session.token' in js
def test_no_inner_html():
    assert "innerHTML" not in js
def test_responsive_forms():
    assert ".admin-form" in css and "@media(max-width:600px)" in css
