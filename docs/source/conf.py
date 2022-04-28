# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(2, os.path.abspath('../..'))




# -- Project information -----------------------------------------------------

project = 'shared_atomic'
copyright = '2022, xiquanren'
author = 'xiquanren'

# The full version, including alpha/beta/rc tags
release = '1.0.11'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "myst_parser",
        "sphinx.ext.autodoc",
        #"sphinx.ext.napoleon",
        #"sphinx_autodoc_typehints",
]



autoclass_content = "both"
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'

html_theme_options = {
    #'logo': 'sharedAtoms.jpg',
    'github_user': 'irvinren',
    'github_repo': 'shared_atomic',
    'description': 'Shared atomicity with multiprocessing/multithreads shared ctypes',
    'donate_url': 'https://paypal.me/xiquanren',

    #'github_banner': 'true',
    'github_button': 'true',
    'show_powered_by': 'false',
    'show_relbars': 'true',
    'caption_font_family': 'serif',
    'code_font_family': 'serif',
    'code_font_size': '19px',
    'font_family': 'serif',
    'font_size': '19px',
    'head_font_family': 'serif',
    #'topic_bg': '#444',
    'page_width': '1280px',
    'sidebar_width': '300px'




    #'fixed_sidebar': "true"
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
  '**': ["about.html",
         "navigation.html",
         "relations.html",
          "searchbox.html",
          "donate.html"
  ]
}
html_title = "Documentation for shared_atomic"
copyright = "2022, Xiquan Ren <xiquanren@yandex.com>"
author = "Xiquan Ren <xiquanren@yandex.com>"
