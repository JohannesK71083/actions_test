from os import environ
with open(environ["GITHUB_ENV"], "a") as f:
    f.write("TEST1<<EOF\ntest\ntest2\ntest3\nEOF")
