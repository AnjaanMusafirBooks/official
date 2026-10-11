# Anjaan Musafir Books — New Version Website Candidate v4

This is the consolidated candidate frontend for the `official` repository on `new-version-candidate`. It is not a production release.

## Candidate safety

- `new-version-config.js` intentionally leaves `API_BASE` and `CHECKOUT_WORKER_URL` blank.
- Configure both only with the dedicated staging Worker HTTPS URL after staging is prepared.
- Cashfree mode defaults to `sandbox`; do not set production mode for this candidate.
- No public page hard-codes the production Worker URL. Checkout, My Order and legacy admin pages do not send requests until the candidate staging URL is configured.
- Do not upload this package to the production `main` branch.

## Included features

- Public website, book catalog, checkout/modal and My Order pages.
- Admin login/dashboard, product and coupon controls, staff/permission UI, reports and email/health/audit screens.
- Purchase Request review, password recovery and Founder-only Maintenance/Backup UI.
- Encrypted database backup download, staging-only merge restore, Owner Control Lock, Safe Mode and technical log retention controls.
- Product cover upload and database-driven New Version book cards; checkout events and advanced order filters.

## Setup

1. Prepare a dedicated staging Worker and apply backend migrations 001–016 to staging D1.
2. Set `API_BASE` and `CHECKOUT_WORKER_URL` in `new-version-config.js` to the staging Worker HTTPS URL.
3. Keep `CASHFREE_MODE` as `sandbox`.
4. Configure CORS, D1/R2 bindings and staging-only secrets on the Worker.
5. Run the local tests and then test in a mobile browser against staging.

## Verification status

Local frontend tests pass at the checkpoint documented in `FINAL_STATUS_AND_TESTS.md`. No browser staging, Cashfree sandbox payment, real Brevo inbox delivery or end-to-end customer PDF delivery has been verified yet.
