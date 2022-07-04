from flask import Flask

def create_web():
	web = Flask(__name__)
	web.config['SECRET_KEY'] = 'ehrgiuveboaBVERGfbiuwbev'

	return web
