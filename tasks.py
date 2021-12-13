from invoke import task
import os

@task()
def build(c):
    print("Nada que construir")

@task()
def test(c):
    os.system("pytest test/test.py")
    os.system("pytest test/test-api.py")

@task()
def install(c):
    os.system("python3 setup.py install --prefix ~/.local")