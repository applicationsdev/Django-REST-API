### About
- RESTful API
- Back End: Django, Python, SQLite

### Get started
Required versions
- Python >= 3
- Django >= 2
- Django REST framework >= 3

<i>installation guides can be found at the official websites</i>

```bash
# In your command line, run the following commands

# Clone the repository inside the desired directory
# (this path will be refered as YOUR_PATH)
git clone --depth 1 git@github.com:applicationsdev/Django-REST-API

# Navigate to the project folder
cd Django-REST-API

# Make the migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create a Django admin account
python3 manage.py createsuperuser

# Run the app
python3 manage.py runserver

# Using your web browser:
# Open the url http://YOUR_PATH/Django-REST-API/admin/
# login to Django admin panel,
# and go to 'Products' section to create a few products in the database.

# To test the RESTful API
# call the url http://YOUR_PATH/Django-REST-API/api/products/
# using command line tools like cURL or HTTPie
# or any HTTP client app like Postman
# or your web browser

```

### License
&copy; [Applications Developer](https://github.com/applicationsdev?tab=repositories), 2018

Author's work is licensed under [MIT](https://opensource.org/licenses/MIT) License | By using this open source product you accept the [license terms](https://opensource.org/licenses/MIT) in full

Frameworks, packages & resources are properties of their respective developers and/or owners & are licensed by them

### Resources - References
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](http://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html)
