## MachineSens ERP Login

Replaces the Frappe / ERPNext login page (`/login`) with a custom **MachineSens ERP**
sign-in screen. Nothing else in the system changes.

- A midnight-indigo, animated two-panel design. On wide screens the left side shows an
  animated ERP story:
  - a live operations card with its chart drawing itself;
  - activity notifications sliding in;
  - module chips linked to the card by moving data packets;
  - a Quote → Order → Procure → Deliver → Invoice → Paid flow;
  - a dock of the ERP modules.
- The right side is a frosted sign-in card with an animated gradient border, a greeting
  based on the visitor's clock, and Email / Password fields.
- On phones and tablets only the sign-in card is shown.
- Works on Frappe / ERPNext **v15** (tested against 15.121) and v16.
- The page is only a new look. Signing in is still done by Frappe's own `login.js`, so
  password login, two-factor (OTP app / SMS / email), "Forgot password?", redirects
  (`?redirect-to=`), LDAP, social logins and email-link login keep working.
- "Remember me" keeps the email on that browser only, never the password.
- Uninstalling the app brings the previous login page back.

### Install

```bash
cd ~/frappe-bench
bench get-app https://github.com/kamal-star/buildot_login
bench --site <your-site> install-app buildot_login
bench build --app buildot_login
bench --site <your-site> clear-cache
bench --site <your-site> clear-website-cache
sudo supervisorctl restart all        # production; use `bench restart` if that is how the server is run
```

### Update (after a new version is pushed)

```bash
cd ~/frappe-bench
bench update --apps buildot_login --pull      # or: cd apps/buildot_login && git pull
bench build --app buildot_login
bench --site <your-site> clear-cache && bench --site <your-site> clear-website-cache
sudo supervisorctl restart all
```

### If the old login still shows

Frappe serves `/login` from the **most recently installed** app that has a
`www/login.html`. If another theme app with its own login page is installed after this
one, it wins. Check the order with `bench --site <your-site> list-apps`;
`buildot_login` must come after any other theme. Reinstalling it puts it last:

```bash
bench --site <your-site> uninstall-app buildot_login --yes --no-backup
bench --site <your-site> install-app buildot_login
bench --site <your-site> clear-cache && bench --site <your-site> clear-website-cache
```

### Uninstall

```bash
bench --site <your-site> uninstall-app buildot_login
bench --site <your-site> clear-cache && bench --site <your-site> clear-website-cache
```

### Files

| File | What it is |
| --- | --- |
| `buildot_login/www/login.html` | The page (layout and the small script that styles Frappe's login states) |
| `buildot_login/www/login.py` | Reuses Frappe's own login context |
| `buildot_login/public/css/buildot_login.css` | All styles and animations (colours are CSS variables at the top) |
| `buildot_login/templates/includes/ms_icons.html` | Icons ([Lucide](https://lucide.dev), ISC licence) |
| `buildot_login/public/images/machinesens-symbol.png` | MachineSens logo mark |

Texts (headline, module names, notifications, footer) are plain text in `login.html`.
The app name in "Sign in to your … ERP workspace" comes from **Website Settings → App
Name**. After editing, run `bench build --app buildot_login` and clear the cache.

#### License

MIT
