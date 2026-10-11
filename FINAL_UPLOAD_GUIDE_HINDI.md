# Basic Version Website (Frontend) — Upload Guide

## Safety first
- Target repository: `official`.
- Target branch: `basic-version`.
- Upload the contents of this package at the repository root (not the containing folder).
- Do not merge to `main`, change GitHub Pages production settings, or publish this candidate to the live site until staging verification is complete.

## Configure staging API
1. Open `new-version-config.js`.
2. Set `API_BASE` to the **staging Worker HTTPS URL only**, for example `https://YOUR-STAGING-WORKER.workers.dev`.
3. Do not put admin keys, bootstrap secrets, Cashfree secrets, or other secrets in this file; it is public.
4. Candidate branch pages may not automatically publish if GitHub Pages is configured for `main`. Use a separate preview deployment/local static server or isolated staging site; do not change production Pages settings just to test.

## Included UI
- `index.html`, `style.css`, `app.js`, `books.js` and legal/contact pages
- `team-login.html` and `team-login.js`
- `admin-dashboard.html`, `.css`, `.js`
- `my-order.html` and content manager pages
- images/assets and frontend source tests

## PDF upload flow
The Admin Dashboard has a separate PDF upload form. It sends a multipart request to `/api/v2/admin/products/upload`, stores the returned private R2 key in the product form, and then saves the product record. This requires staging R2 binding `BOOKS_BUCKET` and a role with `files.manage` permission.

## Test notes
Run frontend source tests with `pytest -q` from this folder. These are source-level tests; they do not prove the real browser-to-Worker request, authentication, payment, or file-delivery path works. Test the whole flow against staging before launch.


## Admin UI CRUD notes
- Books/Products list has Edit and Archive actions. Edit updates name, MRP, selling price and status; other product metadata remains unchanged unless changed through the product create/API workflow.
- Coupons list has Edit and Enable/Disable actions. Edit changes discount type/value, minimum amount and max uses.
- These actions require the staging Worker and the matching server-side permissions.
