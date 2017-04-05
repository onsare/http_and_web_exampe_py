import requests
import json
import web_api
import os

# server running locally
web_api.run_server()

server = 'http://localhost:9000'

print "Creating the message..."
created = None
data = json.dumps("Hello Andela Boot Camp")
req = requests.post(server, data=data)
created = req.json()['created']
print "Message ID: " + str(created)

print "Showing the message..."
req = requests.get(server + '/' + str(created))
print "Response: " + str(req.json())

print "Updating the message..."
data = json.dumps("Goodbye, Andela Boot Camp")
req = requests.put(server + '/' + str(created), data=data)
print "Response: " + str(req.json())

print "Showing the message again..."
req = requests.get(server + '/' + str(created))
print "Response: " + str(req.json())

print "Deleting the message..."
req = requests.delete(server + '/' + str(created))
print "Response: " + str(req.json())

os._exit(0)
