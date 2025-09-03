def log(msg):
	f = open(__file__.replace('.pyc', '.py').replace('Logging.py','Minilab_3_custom.log'), 'a')
	f.write(msg+"\n")
	f.close()