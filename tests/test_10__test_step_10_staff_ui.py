from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "admin-dashboard.html").read_text()
JS = (ROOT / "admin-dashboard.js").read_text()


def test_staff_view_and_permission_controls_exist():
    assert 'id="staff-view"' in HTML
    assert 'id="staff-create-form"' in HTML
    assert 'id="permission-form"' in HTML


def test_staff_endpoints_match_auth_backend_routes():
    assert '/api/v2/admin/staff' in JS
    assert '/api/v2/admin/role-permissions' in JS
    assert 'FOUNDER' in JS


def test_staff_actions_are_explicit_and_confirmed():
    assert '/disable' in JS or '"/"+action' in JS
    assert 'confirm(' in JS
