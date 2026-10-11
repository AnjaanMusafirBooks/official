from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_password_recovery_pages_call_only_candidate_api():
    forgot = (ROOT / "forgot-password.html").read_text()
    reset = (ROOT / "reset-password.html").read_text()
    assert "/api/v2/admin/password-reset/request" in forgot
    assert "/api/v2/admin/password-reset/confirm" in reset
    assert "location.hash.replace" in reset
    assert "name=\"referrer\" content=\"no-referrer\"" in reset
    assert "NM_NEW_VERSION_CONFIG" in forgot and "NM_NEW_VERSION_CONFIG" in reset
    assert "Authorization" not in forgot and "Authorization" not in reset


def test_login_links_to_password_recovery():
    login = (ROOT / "team-login.html").read_text()
    assert 'href="forgot-password.html"' in login
