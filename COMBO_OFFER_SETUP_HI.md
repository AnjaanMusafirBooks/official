# Anjaan Musafir Books — Combo Offer (Hindi Setup Guide)

## इस पैकेज में क्या है

- `admin.html`: Premium Combo Offer Manager — कॉम्बो नाम, वैकल्पिक विवरण, एक या अधिक किताबें, स्वतः MRP/वर्तमान कीमत/सामान्य छूट/अतिरिक्त छूट/बचत, अपनी Combo Price, Active/Inactive, Edit और Disable.
- `combo.js`: वेबसाइट पर प्रीमियम कॉम्बो कार्ड, किताब के कवर/परिचय जहाँ पहचान उपलब्ध हो, “इस किताब में क्या है?” और Combo Checkout.
- `combo-config.js`: एक ही जगह से Worker API और Cashfree mode सेट करने की सुविधा.
- `index.html`, `app.js`, `book.html`, `my-order.html`, `thank-you.html`: config loading और combo payment/delivery presentation से संबंधित बदलाव.
- `COMBO_OFFER_TEST_REPORT_HI.md`: लोकल टेस्ट के परिणाम और वे जाँचें जो अभी लाइव पर नहीं हुई हैं.

## बहुत जरूरी सुरक्षा नियम

1. ये फाइलें तुम्हारे द्वारा अपलोड किए गए ZIP snapshots के आधार पर तैयार हैं। मैंने तुम्हारी लाइव GitHub/Cloudflare production deployment को सीधे नहीं बदला है।
2. `main` branch और production Worker/D1 को untouched रखो।
3. Frontend में `combo-config.js` डिफ़ॉल्ट रूप से मौजूदा production Worker और Cashfree production mode चुनता है। **Staging test शुरू करने से पहले staging Worker URL और `cashfreeMode: "sandbox"` सेट करो।**
4. Staging Worker को अलग D1 database, अलग Worker name, Cashfree sandbox credentials और अलग `FRONTEND_URL` चाहिए। Production D1 पर test orders न बनाओ।
5. `src/index.js` पूरा Worker source है। इसे current production Worker से तुलना किए बिना replace मत करना।
6. D1 migration `002_combo_offers.sql` केवल एक बार उसी test database पर चलानी है। इसमें `ALTER TABLE orders ADD COLUMN combo_id TEXT` है; उसी DB पर दोबारा चलाने से duplicate-column error आएगा।

## Frontend कहाँ रखें

Frontend ZIP के अंदर की फाइलें वेबसाइट repository के root में रखें (यानी `index.html` के समान स्तर पर):

- `admin.html`
- `app.js`
- `index.html`
- `book.html`
- `my-order.html`
- `thank-you.html`
- `combo.js` (नई)
- `combo-config.js` (नई)

`books.js`, `style.css`, covers और बाकी pages को इस पैकेज से overwrite नहीं किया गया है। वे repository में मौजूद रहने चाहिए।

## Staging frontend तैयार करना

1. अलग development branch या अलग staging repository बनाओ।
2. Staging में `combo-config.js` खोलो और `apiBase` को staging Worker URL से बदलो; `cashfreeMode` को `sandbox` रखो।
3. सुनिश्चित करो कि staging pages में `combo-config.js` को `app.js`/`combo.js` से पहले load किया गया है (इस पैकेज में संबंधित pages पर ऐसा किया गया है)।
4. Production branch में यह staging URL या sandbox mode commit न करो। Production में merge करने से पहले config वापस production Worker URL और `production` mode पर होना चाहिए।

## Backend कहाँ रखें

Backend ZIP में:

- `src/index.js` — Worker code (पूरी फाइल; staging branch में ही पहले इस्तेमाल करें)
- `db/migration/002_combo_offers.sql` — नई D1 migration
- `wrangler.staging.example.jsonc` — केवल staging config का उदाहरण; placeholders बदलने से पहले deploy न करें

Worker repository में paths ठीक इसी तरह होने चाहिए। Existing `wrangler.jsonc`, production database ID और production secrets को overwrite नहीं करना है।

## Staging Worker और D1 का सुरक्षित क्रम

1. Cloudflare में अलग staging D1 database बनाओ।
2. उस test DB में मौजूदा schema और जरूरी existing migrations लगाओ। केवल products/offers जैसे non-customer catalog data की test copy रखो; production customer orders, download tokens और PII copy मत करो।
3. `002_combo_offers.sql` को test DB पर एक बार चलाओ। Migration existing rows delete नहीं करती; orders table में `combo_id` column और combo/order-item tables जोड़ती है।
4. `wrangler.staging.example.jsonc` की copy `wrangler.staging.jsonc` बनाओ। `database_id`, staging Worker URL और staging Frontend URL भरें; `CASHFREE_ENV` को `sandbox` रखें।
5. Sandbox Cashfree credentials और अलग `ADMIN_KEY` staging Worker secrets के रूप में सेट करो। Secrets GitHub files में मत लिखो। Email delivery को staging में disable रख सकते हो ताकि असली ग्राहक को test email न जाए।
6. Staging Worker deploy करो और staging frontend config में उसका URL डालो।
7. टेस्ट पूरा होने के बाद ही diff review और तुम्हारी स्पष्ट अनुमति से production rollout की योजना बनाओ।

## Combo Manager में क्या होगा

- जितने चाहो कॉम्बो बना सकते हो; हर कॉम्बो में एक या अधिक सक्रिय किताबें चुन सकते हो।
- कुल MRP और मौजूदा बिक्री मूल्य चुनी गई किताबों से निकलते हैं।
- सामान्य छूट, Combo Price से अतिरिक्त छूट, बचत और MRP से कुल छूट अलग दिखाई जाती है।
- Combo Price Admin खुद तय करता है। Browser से भेजी गई कीमत को backend स्वीकार नहीं करता; कीमत D1 में सेव कॉम्बो से ली जाती है।
- कॉम्बो में चुनी गई हर किताब का अलग download link होता है और हर किताब की download limit अलग लागू होती है।
- किसी कॉम्बो में किताब inactive हो जाए तो पूरा कॉम्बो storefront से छिपता है और checkout reject होता है; partial combo नहीं बेचा जाता।

## मौजूदा सीमा

- Combo checkout पर coupon apply नहीं होता; existing single-book coupon logic को जानबूझकर नहीं बदला गया है।
- Cashfree sandbox/production, वास्तविक R2/PDF assets और वास्तविक email provider के साथ end-to-end live test इस पैकेज निर्माण में नहीं किया गया। लोकल mock tests पास हुए हैं; नीचे test report देखें।
