from setuptools import setup


setup(
    name='PEA_auth',
    version='1.0',
    description="Simple authentication module for PEA user accounts",
    url="https://github.com/Exeter/PEA_auth",
    download_url="https://github.com/Exeter/PEA_auth",
    author="Sean Lee",
    author_email="freshdried@gmail.com",
    install_requires=["requests>=1.1.0"],
    packages=['PEA_auth'],
)
