app_name = "buildot_login"
app_title = "BuildOT Login"
app_publisher = "MachineSens IoT"
app_description = "BuildOT One login page for Frappe / ERPNext"
app_email = "info@machinesensiot.com"
app_license = "mit"

# Nothing else is hooked. The app only ships www/login.html + login.py, which
# Frappe serves instead of its own /login because a later-installed app's www/
# page takes precedence. Uninstalling the app brings the previous login back.
