# DevSearch
# live-link: http://ec2-18-142-56-106.ap-southeast-1.compute.amazonaws.com/
Devsearch is a dynamic platform crafted to connect developers through project sharing, feedback, and collaboration. With Devsearch, users can showcase their work, connect with like-minded developers, and engage in meaningful discussions through an integrated chat feature. The platform also enables users to rate each other's work, promoting a culture of recognition and constructive critique. Devsearch’s powerful search functionality allows developers to find others based on skill sets, interests, or specific project types, making it easy to build networks, collaborate on projects, or seek guidance within the developer community.

# Installation
- 1 - clone repo
- 2 - create a virtual environment and activate
- - pip install virtualenv
- - virtualenv envname
- - envname\scripts\activate
- 3 - cd into project "cd devsearch-demo"
- 4 - pip install -r requirements.txt
- 5 - run the server
- - python manage.py runserver / docker-compose up --build(if you have docker and docker-compose installed on your system)

# Features
- Share Projects
- Chat with other developers.
- Rate other's work
- Search for other developers.

# Tech Stack
- Django
- Postgres
- Django REST Framework
