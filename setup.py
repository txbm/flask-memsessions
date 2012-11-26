"""
Flask Memsessions
-----------------

A simple extension to drop in memcached sessions using the 
existing Werkzeug cache interface.

Links
`````

* `development version
  <http://github.com/petermelias/flask-memsessions/zipball/master#egg=Flask-Memsessions-dev>`_



"""

from setuptools import setup

setup(
	name='Flask-Memsessions',
	version='0.1',
	url='http://github.com/petermelias/flask-memsessions',
	license='BSD',
	author='Peter M. Elias',
	author_email='petermelias@gmail.com',
	description='A simple extension to drop in memcached session support for Flask.',
	long_description=__doc__,
	py_modules=['flask_memsessions'],
	zip_safe=False,
	include_package_data=True,
	platforms='any',
	install_requires=[
		'Flask',
		'Werkzeug',
		'python-memcached',
	],
	classifiers=[
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	test_suite='tests'
)