=======
back
=======

Fileupload is a app to upload files.

Quick start
-----------

1. Add "back" to your INSTALLED_APPS setting like this::
        INSTALLED_APPS = [
                ...
                'back',
        ]

2. Include the polls URLconf in your project urls.py like this::
        path('back/',include('back.urls'),name='back'),

3. Run "python manage.py migrate" to create the models.