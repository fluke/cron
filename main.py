import requests
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/daily')
def daily():
    return requests.get('http://yourcompany.com/cron/?password=longstringshouldprobablyberandom&period=daily', verify=True).content

@app.route('/bimonthly')
def bimonthly():
    return requests.get('http://yourcompany.com/cron/?password=longstringshouldprobablyberandom&period=bimonthly', verify=True).content

@app.route('/monthly')
def monthly():
    return requests.get('http://yourcompany.com/cron/?password=longstringshouldprobablyberandom&period=monthly', verify=True).content

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
