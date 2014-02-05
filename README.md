#PEA_auth
A python module for authentication on the PEA network.

##installation
`pip install git+git://github.com/Exeter/PEA_auth.git `

##usage

```python
from PEA_auth import auth
username = "blah"
password = "blah"
if auth(username, password):
	print('yay authenticated')
else print('nay')
```
