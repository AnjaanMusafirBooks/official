# Candidate v22 — Local Status and Test Results

Date: 2026-10-11

## Latest local checks
- Backend pytest: **161 passed**.
- Frontend pytest: **43 passed**.
- `node --check` passed for backend `src/*.js`, backend `website/*.js`, and frontend root `*.js`.
- Baseline `db/schema.sql` plus migrations 001–018 applied successfully in an in-memory SQLite smoke test.

## Candidate v22 coupon counter underflow guard
- Coupon release and redemption now decrement `reserved_count` only when it is greater than zero.
- Removed `MAX(0, reserved_count - 1)` from these reservation-resolution paths; inconsistent counters will now fail guarded updates and be surfaced instead of silently clamped.
- Added two regression tests for release/redemption underflow protection.
- Earlier missing-coupon, concurrent-resolution, paid-order recovery, and safe coupon-delete protections remain included.

## Not verified yet
- Cloudflare D1 runtime and real concurrent transaction behavior.
- Cashfree Sandbox payment/webhook and complete purchase-to-download.
- R2 private PDF access, token expiry/usage limits, Brevo inbox delivery, and Android/browser staging.
- Full admin permission allow/deny matrix and Current Version regression against a faithful staging baseline.
- Production Worker, production D1, production secrets and production `main` were not changed.
