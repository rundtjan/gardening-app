from invoke import task

@task
def build(ctx):
    ctx.run("mkdir data; py src/db_init.py")

@task
def start(ctx):
    ctx.run("py src/index.py")

@task
def alt_build(ctx):
    ctx.run("mkdir data; python3 src/db_init.py")

@task
def alt_start(ctx):
    ctx.run("python3 src/index.py")
