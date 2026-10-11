from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "admin-dashboard.html").read_text()
JS = (ROOT / "admin-dashboard.js").read_text()

def test_pdf_upload_form_exists():
    assert 'id="product-pdf-upload-form"' in HTML
    assert 'accept="application/pdf,.pdf"' in HTML
    assert 'id="product-pdf-file-key"' in HTML

def test_upload_uses_form_data_and_bearer_session():
    assert 'new FormData()' in JS
    assert '"/api/v2/admin/products/upload"' in JS
    assert 'Authorization:"Bearer "+session.token' in JS
    assert 'Content-Type' not in JS[JS.find('async function uploadProductPdf'):JS.find('async function createProduct')]

def test_uploaded_key_is_saved_into_product_form():
    assert '$("product-pdf-file-key").value=result.pdf_file_key' in JS
    assert '$("product-pdf-upload-form").addEventListener("submit",uploadProductPdf)' in JS
