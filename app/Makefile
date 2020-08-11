
default:
	echo ...

test:
	@echo cleanup __pycache__ folders
	@find src tests -name __pycache__ -exec rm -rf {} \;
	@echo run tests
	@pytest -v

