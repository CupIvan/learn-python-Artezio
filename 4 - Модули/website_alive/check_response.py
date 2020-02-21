from .make_request import func as mr

def func(url):
	try:
		res = mr(url)
	except:
		return False
	return res.status_code == 200
