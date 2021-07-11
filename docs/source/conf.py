import datetime
import os
import sys


sys.path.insert(0, os.path.abspath("../../src"))
sys.path.append(os.path.abspath("./demo/"))

project = "sphinx-benjcunningham-theme"
copyright = "{}, {}.".format(datetime.datetime.now().year, Ben Cunningham)
author = "Ben Cunningham"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_multiversion",
    "sphinx_benjcunningham_theme",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_benjcunningham_theme"

smv_branch_whitelist = r"^(master|develop|release\/.*)$"
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"
smv_released_pattern = r"^.*(tags|master).*$"
smv_remote_whitelist = r"^(origin)$"
