from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'admin-dashboard.html').read_text()
js = (ROOT / 'admin-dashboard.js').read_text()
css = (ROOT / 'admin-dashboard.css').read_text()
def test_all_views_have_sections():
    for name in ['overview','products','coupons','orders','customers','reports']:
        assert f'id="{name}-view"' in html
        assert f'data-view="{name}"' in html

def test_api_paths_are_known_candidate_routes():
    for path in ['/api/v2/admin/me','/api/v2/admin/products','/api/v2/admin/coupons','/api/v2/admin/orders','/api/v2/admin/customers','/api/v2/admin/reports/summary','/api/v2/admin/reports/orders.csv']:
        assert path in js

def test_auth_and_no_demo_metrics():
    assert 'Authorization:\"Bearer \"+session.token' in js
    assert 'nm_admin_session_v2' in js
    assert 'demo' not in js.lower()

def test_mobile_styles_exist():
    assert '@media(max-width:850px)' in css
    assert '@media(max-width:440px)' in css
