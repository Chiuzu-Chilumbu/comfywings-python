from invoke import task

@task
def quality(c):
	c.run('find . -type f -name "*.py" | xargs pylint ')