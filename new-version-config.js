/* New Version candidate configuration.
 * Set API_BASE only to the isolated staging Worker URL, never production by accident.
 * This value is public configuration, not a secret.
 */
window.NM_NEW_VERSION_CONFIG = Object.freeze({
  API_BASE: "",
  // Set only to the isolated candidate/staging Worker; never production by default.
  CHECKOUT_WORKER_URL: "",
  CASHFREE_MODE: "sandbox"
});
