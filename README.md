# My Blog App


### Table of Contents
- [Description](#description)
- [Features](#features)
- [Installing](#installing)
***
## Description
The project done during learning Django framework. 
With this app you can publish post, share via email and leave a comments. 
***
## Features
* Post list (with pagination) , adding comments to a post, recommending similar posts(tagging system). 
* Admin panel (with filters , search , editing and etc).
* Retrieving posts by similarity(by tags).
* Custom template tags and filters.
* Sitemap.
* Post feeds(RSS).
* Sharing posts via email.
* Custom template tags.
* Custom template filters.
***
## Installing

Clone the project:
```
git clone https://github.com/davkdev620/myblog.git
```

Install the requirements.txt file:
```
pip install -r requirements.txt
```

Make migration:
```
python manage.py makemigrations
python manage.py migrate
```

Crate super user:
```
python manage.py createsuperuser
```

Add some post to the blog.

or

You can load fixture into your database, instead adding posts by yourself.
To load the fixture run:
```
python manage.py loaddata posts.json 
```

To run the app on local host: 
```
python manage.py runserver
```
Open your browser with 127.0.0.1:8000/blog/ url, to see your posts.


For sharing post via mail , pls config settings for your email (at settings.py and views.py).


___For production use, before publish the project, change the SECRET_KEY. It’s recommended to set it as local variable!___ 

