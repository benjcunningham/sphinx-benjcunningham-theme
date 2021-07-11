import os


def get_html_theme_path():

    return os.path.abspath(os.path.dirname(__file__))


def builder_inited(app):

    static_path = os.path.join(get_html_theme_path(), "static")

    app.config.html_static_path.append(static_path)
    app.config.html_logo = "logo.svg"


def setup(app):

    theme_path = get_html_theme_path()

    app.add_html_theme("sphinx_benjcunningham_theme", theme_path)
    app.add_css_file("custom.css")

    app.connect("builder-inited", builder_inited)
