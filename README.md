# YWasteFood

To run this project, you need to install Python. Then you need to install some packages.<br>
Please Run:<br>

```
pip install -r requirements.txt
```

<br><br>
To run this application, go to the project folder and open a terminal window and run:

```
python manage.py runserver
```

Then go to <http://localhost:8000>
<br>
<br>
Replace Secret Key, Email Information and tawk.to API key with your own.

<br><br>

Admin Panel Info:<br>
Username: admin<br>
Password: admin1234
<br>
<br>
You can create a new superuser by running

```
python manage.py createsuperuser
```

<br>
<br>

# if no data display on Food Donate section the follow below instruction to add the data

Open the shell:

```
python manage.py shell
```
Execute the following commands to create new Data in project model:

```
from projects.models import project
```


# Add a new project
```
project.objects.create(title="Project 1", description="Description for Project 1")
project.objects.create(title="Project 2", description="Description for Project 2")
```

# Verify the added projects
```project.objects.all()```