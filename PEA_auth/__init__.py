import requests

def _webmail_auth(uname, pword):
	"""
	Uses webmail.exeter.edu basic authentication

	Returns True if authentication succeeds
	Return False if authentication fails
	"""
	url = "https://webmail.exeter.edu/exchweb/bin/auth/owaauth.dll"
	payload = {"destination": "https://webmail.exeter.edu/exchange", "username": uname, "password":  pword, "SubmitCreds": "Log On"}
	r = requests.post(url, data=payload)
	if r.url == "https://webmail.exeter.edu/exchange/":
		return True
	return False

def auth(uname, pword):
	"""
	Returns True if authentication succeeds
	Return False if authentication fails
	"""
	return _webmail_auth(uname,pword)
