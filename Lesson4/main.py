#!/bin/env python

from website_alive import check_response

def func():
	print("Enter site: ", end='')
	url = input()

	if not "http" in url:
		url = "http://" + url

	print("Site is online" if check_response.func(url) else "Site is offline")

func()
