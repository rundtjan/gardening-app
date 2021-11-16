from invoke import task

@task
def start(ctx):
    ctx.run("py src/index.py")
