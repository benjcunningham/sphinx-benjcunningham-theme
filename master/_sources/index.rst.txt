***************************
sphinx-benjcunningham-theme
***************************

Custom Sphinx theme baed on the ubiquitous `Read the Docs
<https://github.com/readthedocs/sphinx_rtd_theme>`_ theme. It overrides the Read the
Docs theme with custom components and styles.

Installation
============

Install the theme by adding the following to your library's ``setup.py``:

.. code:: python

    from setuptools import setup


    extras = {
        ...
        "docs": [
            "sphinx_benjcunningham_theme @ https://github.com/benjcunningham/sphinx-benjcunningham-theme",
        ],
    }

    setup(
        ...
        extras_require=extras,
    )

In your Sphinx ``conf.py``, make sure to include the following:

.. code:: python

    extensions = [
        ...
        "sphinx_benjcunningham_theme",
    ]

    html_theme = "sphinx_benjcunningham_theme"

Either build the documentation from your current branch using a tradition Sphinx build
script, or build a versioned site using the following:

.. code:: bash

    sphinx-multiversion docs/source docs/build

.. toctree::
    :caption: Demo Documentation
    :hidden:

    demo/structure
    demo/demo
    demo/list_tables
    demo/api
