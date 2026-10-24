# Controller for the MachineSens ERP login page. It reuses Frappe's own login context
# unchanged, so redirects for logged-in users, social logins, LDAP, email-link
# login and the sign-up setting all behave exactly as on the standard page.

from frappe.www.login import get_context as frappe_login_context

import buildot_login

no_cache = 1


def get_context(context):
	context = frappe_login_context(context)
	context.bo_version = buildot_login.__version__
	return context
