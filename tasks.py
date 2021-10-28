from invoke import task
import os

@task()
def test(c):
    os.system("pytest tests/test.py")
