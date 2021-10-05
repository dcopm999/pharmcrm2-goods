=============================
PharmCRM2: Goods
=============================

.. image:: https://badge.fury.io/py/pharmcrm2-goods.svg
    :target: https://badge.fury.io/py/pharmcrm2-goods

.. image:: https://travis-ci.org/dcopm999/pharmcrm2-goods.svg?branch=master
    :target: https://travis-ci.org/dcopm999/pharmcrm2-goods

.. image:: https://codecov.io/gh/dcopm999/pharmcrm2-goods/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/pharmcrm2-goods

PharmCRM2: Goods

Documentation
-------------

The full documentation is at https://pharmcrm2-goods.readthedocs.io.

Quickstart
----------

Install PharmCRM2: Goods::

    pip install pharmcrm2-goods

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        "goods",
        ...
    )

Add PharmCRM2: Goods's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path("goods/", include("goods.urls", namespace="goods")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
