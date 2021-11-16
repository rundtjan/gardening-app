from invoke import task

@task
def build(ctx):
    ctx.run("mkdir data")
    ctx.run("py src/db_init.py")

@task
def start(ctx):
    ctx.run("py src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def alt_build(ctx):
    ctx.run("mkdir data")
    ctx.runt("python3 src/db_init.py")

@task
def alt_start(ctx):
    ctx.run("python3 src/index.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")