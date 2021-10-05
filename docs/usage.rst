=====
Usage
=====

To use PharmCRM2: Goods in a project, add it to your `INSTALLED_APPS`:

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
