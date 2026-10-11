from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_admin_product_form_uploads_cover_and_saves_asset_key():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'id="product-cover-upload-form"' in html
    assert 'id="product-cover-asset"' in html
    assert 'id="product-cover-preview"' in html
    assert '/api/v2/admin/products/cover-upload' in js
    assert 'cover_asset:x.cover_asset.trim()||null' in js


def test_public_catalog_merges_database_managed_products():
    app = (ROOT / "app.js").read_text()
    assert "bySlug[item.slug] = item" in app
    assert "New database-managed books are rendered without requiring a code edit." in app
    assert "PRODUCT_IDS[d.slug] = d.product_id || id" in app


def test_product_form_can_adopt_existing_stable_product_id():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'name="product_id"' in html
    assert 'product_id:x.product_id.trim()||null' in js


def test_product_edit_form_covers_full_metadata_without_changing_slug_or_id():
    html = (ROOT / "admin-dashboard.html").read_text()
    js = (ROOT / "admin-dashboard.js").read_text()
    assert 'id="product-edit-form"' in html
    assert 'name="offer_starts_at"' in html and 'name="offer_ends_at"' in html
    assert 'name="slug" pattern="[a-z0-9]+(?:-[a-z0-9]+)*" maxlength="120" required readonly' in html
    assert 'function saveProductEdit(ev)' in js
    assert 'method:"PATCH"' in js and 'encodeURIComponent(id)' in js
