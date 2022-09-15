# This file is placed in the Public Domain.


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="opbot",
    version="102",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    url="http://github.com/bthate/opbot",
    description="operator bot",
    long_description=read(),
    license="Public Domain",
    packages=["op", "opb", "opr"],
    scripts=["bin/opbot"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
