import grequests


req = grequests.get('http://www.codehenge.net/blog', hooks=dict(response="11"))
job = grequests.send(req, grequests.Pool(1))

for i in range(10):
    print (i)