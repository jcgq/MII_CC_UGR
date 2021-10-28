from invoke import task
import os

@task()
def test(c):
    os.system("pytest test/test.py")

@task()
def installdeps(c):
    os.system("pip3 install -r requirements/requirements.txt")