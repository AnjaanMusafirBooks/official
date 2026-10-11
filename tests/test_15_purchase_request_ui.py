from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_admin_dashboard_exposes_purchase_requests_view():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'data-view="purchase-requests"' in html
    assert 'id="purchase-requests-view"' in html
    assert 'id="load-purchase-requests"' in html
    assert '/api/v2/admin/purchase-requests?limit=100' in js
    assert '/approve' in js and '/reject' in js


def test_public_request_form_warns_that_request_is_not_payment_verification():
    html = (ROOT / "purchase-request.html").read_text()
    assert 'apiBase' in html or 'const cfg=window.NM_NEW_VERSION_CONFIG' in html
    assert '/api/v2/purchase-requests' in html
    assert 'Admin payment record जाँचने के बाद ही order approve करेगा' in html
    assert 'API_BASE' in (ROOT / "new-version-config.js").read_text()


def test_request_ui_never_sends_admin_token_from_public_form():
    html = (ROOT / "purchase-request.html").read_text()
    assert "Authorization" not in html
