from invoke import task
import os

@task()
def test(c):
    os.system("pytest test/test.py")
    os.system("pytest test/test-api.py")

@task()
def installdeps(c):
    os.system("python3 setup.py install --prefix ~/.local")