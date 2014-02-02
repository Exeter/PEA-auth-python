from PEA_auth import auth
from getpass import getpass
print(auth(input("Username: "), getpass()))
