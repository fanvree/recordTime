import os
from setuptools import find_packages,setup

with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
    name='django-fileapp',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License', # example license
    description='A simple Django app to upload files',
    long_description=README,
    url='https://www.example.com/',
    author='your name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
   ],
)