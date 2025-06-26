def log(msg):
	f = open(__file__.replace('.pyc', '.py').replace('Logging.py','SelectedTrackControl.log'), 'a')
	f.write(msg+"\n")
	f.close()