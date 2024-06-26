# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.sep.join(['..', '..', 'src'])))
import nncli

# -- Project information -----------------------------------------------------

project = 'nncli'
copyright = '2018-2022, Daniel Moch'
author = 'Daniel Moch'

# The short X.Y version
version = nncli.__version__
# The full version, including alpha/beta/rc tags
release = nncli.__version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx_sitemap',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['usage/*', 'configuration/*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'bw'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'
html_extra_path = ['robots.txt']

html_baseurl = 'https://nncli.org/'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'nav_title': 'NextCloud Notes Command Line Interface',
   'base_url': 'https://nncli.org/',

    # Set the color and the accent color
    'color_primary': 'grey',
    'color_accent': 'blue',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/djmoch/nncli/',
    'repo_name': 'Git Repository',
    'repo_type': None,

    'logo_icon': '&#xe261',
    'master_doc': False,

    'nav_links': [
        {'title': 'Home', 'href': 'index', 'internal': True},
        {'title': 'Index', 'href': 'genindex', 'internal': True},
    ],

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': -1,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {'**': ['globaltoc.html', 'localtoc.html', 'searchbox.html']}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'nnclidoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (None, 'nncli.tex', 'nncli Documentation',
     'Daniel Moch', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('nncli.1', 'nncli', 'NextCloud Notes Command Line Interface',
     [author], 1),
    ('nncli-sync.1', 'nncli-sync', 'Sync a NextCloud Notes Database',
     [author], 1),
    ('nncli-list.1', 'nncli-list', 'List Notes In a NextCloud Notes Database',
     [author], 1),
    ('nncli-export.1', 'nncli-export', 'Export Notes From a NextCloud Notes Database',
     [author], 1),
    ('nncli-dump.1', 'nncli-dump', 'Print a NextCloud Note',
     [author], 1),
    ('nncli-create.1', 'nncli-create', 'Create a New NextCloud Note',
     [author], 1),
    ('nncli-import.1', 'nncli-import', 'Import Notes To a NextCloud Notes Database',
     [author], 1),
    ('nncli-edit.1', 'nncli-edit', 'Edit a NextCloud Note',
     [author], 1),
    ('nncli-delete.1', 'nncli-delete', 'Delete a NextCloud Note',
     [author], 1),
    ('nncli-favorite.1', 'nncli-favorite', 'Favorite a NextCloud Note',
     [author], 1),
    ('nncli-cat.1', 'nncli-cat', 'Operate on a NextCloud Note\'s Category',
     [author], 1),
    ('nncli.config.5', 'nncli.config', 'Configuration File For nncli(1)',
     [author], 5),
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (None, 'nncli', 'nncli Documentation',
     author, 'nncli', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'urwid': ('http://urwid.org', None)}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Extension interface -----------------------------------------------------
def setup(app):
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
