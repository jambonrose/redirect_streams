test:
	py.test -v -m tryfirst --maxfail=1
	py.test -v -m "not tryfirst"
