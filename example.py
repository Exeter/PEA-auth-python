from PEA_auth import auth
from getpass import getpass
print(auth(raw_input("Username: "), getpass()))
