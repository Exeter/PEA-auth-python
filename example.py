from PEA_auth import auth
from getpass import getpass

#The simplest example possible

print(auth(input("Username: "), getpass()))
