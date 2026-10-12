/* Anjaan Musafir Books environment config.
   Production defaults preserve the current live setup.
   For staging ONLY, set apiBase to the staging Worker URL and cashfreeMode to "sandbox".
   Never commit staging settings to the production branch. */
window.AM_COMBO_CONFIG = window.AM_COMBO_CONFIG || {
  apiBase: "https://anjaan-musafir-delivery.officialsuperswagg.workers.dev",
  cashfreeMode: "production"
};
