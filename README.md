## BuildOT Login

Replaces the Frappe / ERPNext login page (`/login`) with the **BuildOT One** sign-in
screen (https://buildot.machinesensiot.ai). Nothing else in the system changes.

- Works on Frappe / ERPNext **v15** (tested against 15.121) and v16.
- The page is only a new look: signing in is still done by Frappe's own `login.js`, so
  password login, two-factor (OTP app / SMS / email), "Forgot password?", redirects
  (`?redirect-to=`), LDAP, social logins and email-link login keep working.
- "Remember me" keeps the username on that browser only (never the password), as on
  BuildOT.
- Uninstalling the app brings the previous login page back.

### Install

```bash
cd ~/frappe-bench
bench get-app https://<your-git-host>/buildot_login.git   # or copy the folder into apps/ (see below)
bench --site <your-site> install-app buildot_login
bench build --app buildot_login
bench --site <your-site> clear-cache
bench --site <your-site> clear-website-cache
sudo supervisorctl restart all        # production; use `bench restart` if that is how the server is run
```

Without a git host, copy the `buildot_login` folder into `~/frappe-bench/apps/`, then:

```bash
cd ~/frappe-bench
./env/bin/pip install -e apps/buildot_login
grep -qx buildot_login sites/apps.txt || printf '\nbuildot_login' >> sites/apps.txt
bench --site <your-site> install-app buildot_login
bench build --app buildot_login
bench --site <your-site> clear-cache && bench --site <your-site> clear-website-cache
sudo supervisorctl restart all
```

(`sites/apps.txt` usually has no trailing newline, hence the `printf '\n…'`.)

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
| `buildot_login/www/login.html` | The page (layout + the small script that styles Frappe's login states) |
| `buildot_login/www/login.py` | Reuses Frappe's own login context |
| `buildot_login/public/css/buildot_login.css` | All styles and animations |
| `buildot_login/public/images/buildot-symbol.png` | BuildOT logo |

Texts (headline, "Welcome back", badges, footer) are plain text in `login.html` and can
be edited there. After editing, run `bench build --app buildot_login` and clear the cache.

#### License

MIT
