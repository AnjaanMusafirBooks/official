from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_checkout_activity_tab_and_filters_are_connected():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'data-view="checkout"' in html
    assert 'id="checkout-events-data"' in html
    for field in ["checkout-order-id", "checkout-attempt-id", "checkout-product-id", "checkout-event-type", "checkout-from", "checkout-to"]:
        assert f'id="{field}"' in html
    assert '/api/v2/admin/checkout-events' in js
    assert 'checkout:"Checkout Activity"' in js
