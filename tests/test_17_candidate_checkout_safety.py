from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_candidate_checkout_never_defaults_to_production_worker_or_cashfree():
    app = (ROOT / "app.js").read_text()
    config = (ROOT / "new-version-config.js").read_text()
    assert "CHECKOUT_WORKER_URL" in app
    assert 'CASHFREE_MODE = window.NM_NEW_VERSION_CONFIG?.CASHFREE_MODE === "production" ? "production" : "sandbox"' in app
    assert 'CHECKOUT_WORKER_URL: ""' in config
    assert 'CASHFREE_MODE: "sandbox"' in config
    assert "https://anjaan-musafir-delivery.officialsuperswagg.workers.dev" not in app


def test_payment_error_has_manual_fallback_and_zero_payment_not_started_if_unconfigured():
    app = (ROOT / "app.js").read_text()
    assert "manualFallbackProductId" in app
    assert "purchase-request.html?product_id=" in app
    assert "अभी payment शुरू नहीं की गई है" in app


def test_public_pages_load_candidate_config_before_checkout_script():
    for name in ["index.html", "book.html", "thank-you.html"]:
        html = (ROOT / name).read_text()
        assert html.index('src="new-version-config.js"') < html.index('src="app.js"')


def test_legacy_admin_and_my_order_pages_do_not_hardcode_production_worker():
    for name in ["admin.html", "content-manager.html", "my-order.html"]:
        html = (ROOT / name).read_text()
        assert "https://anjaan-musafir-delivery.officialsuperswagg.workers.dev" not in html
        assert "CHECKOUT_WORKER_URL" in html
        assert "new-version-config.js" in html
