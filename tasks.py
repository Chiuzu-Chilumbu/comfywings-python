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
def unit_tests(c):
	"""
	method to run unit tests with verbose flag
	"""
	c.run('pytest -v tests/unit_tests/test_units_amadeus.py')


@task
def integration_tests(c):
	"""
	method to run integration test with verbose flag
	"""
	c.run('pytest -v tests/integration_tests/test_integration_amadeus.py')


@task
def all_tests(c):
	"""
	method to run all tests
	"""
	c.run('pytest -v tests')


@task
def coverage(c):
	"""
	Run trests with coverage and store results in coverage directory
	"""
	c.run('coverage run -m pytest -v tests')
	c.run('coverage html -d coverage')