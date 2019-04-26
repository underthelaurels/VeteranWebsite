# Data to Init

jobs = [
    {
        "title": "Job 1",
        "description": "Description of job 1\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
    {
        "title": "Job 2",
        "description": "Description of job 2\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
    {
        "title": "Job 3",
        "description": "Description of job 3\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
    {
        "title": "Job 4",
        "description": "Description of job 4\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
    {
        "title": "Job 5",
        "description": "Description of job 5\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
    {
        "title": "Job 6",
        "description": "Description of job 6\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
    {
        "title": "Job 7",
        "description": "Description of job 7\ncould be multiple lines.",
        "street_address": "1234 West Campus Drive",
        "city":"Blacksburg",
        "state":"Virginia",
        "zipcode":23024,
        "industry":"Automated Testing",
        "due_date":"2018-05-08"
    },
]

users = [
    {
        "username":"ctom96",
        "isEmployer":False,
        "password":"chris",
        "first_name":"Chris",
        "last_name":"Tomasello",
        "email":"email@gmail.com"
    },
    {
        "username":"agile",
        "isEmployer":True,
        "password":"enhanced",
        "first_name":"Group",
        "last_name":"3",
        "email":"email@gmail.com"
    },
    {
        "username":"laurel",
        "isEmployer":False,
        "password":"laurel",
        "first_name":"A G I L E",
        "last_name":"E N H A C N E D",
        "email":"email@gmail.com"
    },
    {
        "username":"andrew",
        "isEmployer":False,
        "password":"andrew",
        "first_name":"A G I L E",
        "last_name":"E N H A C N E D",
        "email":"email@gmail.com"
    },
    {
        "username":"shawn",
        "isEmployer":False,
        "password":"shawn",
        "first_name":"A G I L E",
        "last_name":"E N H A C N E D",
        "email":"email@gmail.com"
    },
    {
        "username":"kyle",
        "isEmployer":False,
        "password":"kyle",
        "first_name":"A G I L E",
        "last_name":"E N H A C N E D",
        "email":"email@gmail.com"
    },
    {
        "username":"chris",
        "isEmployer":False,
        "password":"chris",
        "first_name":"A G I L E",
        "last_name":"E N H A C N E D",
        "email":"email@gmail.com"
    },
]

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(0)

    ip = sys.argv[1]
    
    for job in jobs:
        print "Posting job", job['title']
        r = requests.post('http://'+ip+'/employment/add-job', data=job)
    
    for user in users:
        print "posting user", user['username']
        requests.post('http://'+ip+'/user/register', data=user)