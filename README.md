twentytab-treeeditor
====================

A django app that provides FeinCMS admin tree editor.


## Installation

Use the following command: <b><i>pip install twentytab-treeeditor</i></b>

## Configuration

- settings.py

```py
INSTALLED_APPS = {
    ...,
    'treeeditor',
    ...
}
```

- Static files

Run collectstatic command or map static directory.

** This app overrides {% block filters %} in change_list.html template. **