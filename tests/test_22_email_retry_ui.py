from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_email_activity_has_manual_retry_action():
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'target==="email-activity-data"' in js
    assert 'textContent="Retry email"' in js
    assert '/api/v2/admin/email-activity/"+encodeURIComponent(orderId)+"/retry' in js
    assert 'Provider acceptance inbox delivery की guarantee नहीं है' in js
