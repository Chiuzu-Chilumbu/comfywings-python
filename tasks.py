"""
import tasks from invoke
"""
from invoke import task

"""
tasks.py file for automating commands
"""

@task
def quality(c):
	"""
	method to check for code quality
	"""
	c.run('find . -type f -name "*.py" | xargs pylint ')

@task
def specs(c):
	"""
	method to run spec files
	"""
	c.run('pipenv run specs')
