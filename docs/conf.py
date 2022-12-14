# This file is placed in the Public Domain.
# -*- coding: utf-8 -*-


import doctest
import sys
import os


curdir = os.getcwd()

sys.path.insert(0, curdir)
sys.path.insert(0, os.path.abspath(os.path.join(curdir, '..')))

import opb
import opl
import opr
import alabaster


__version__ = '102'


nitpick_ignore = [
                ('py:class', 'builtins.BaseException'),
               ]


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]


project = 'OPBOT'
version = '%s' % __version__
release = '%s' % __version__
needs_sphinx = '5.1.1'
html_short_title = 'operator bot'
html_title = 'OPBOT'
html_style = 'opbot.css'
html_static_path = ['_static',]
html_css_files = ['opbot.css',]
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_theme_options = {
    'github_user': 'bthate',
    'github_repo': 'opbot',
    'github_button': True,
    'github_banner': False,
    'logo': 'opbotsmile.png',
    'link': '#000',
    'link_hover': '#000',
    'nosidebar': True,
    'show_powered_by': False,
    'show_relbar_top': False
}
html_favicon = 'opbotsmile.png'
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = False
html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'relations.html'
    ]
}
html_use_index = False
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = False
#html_use_opensearch = 'http://opbot.rtfd.io/'
html_file_suffix = '.html'
htmlhelp_basename = 'pydoc'
templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
language = 'en'
today = ''
today_fmt = ''
exclude_patterns = ['_build', '_sources', '_templates']
default_role = ''
add_function_parentheses = False
add_module_names = False
show_authors = False
pygments_style = 'colorful'
modindex_common_prefix = ['']
keep_warnings = True
rst_prolog = '''.. image:: opbotline.png
    :width: 100%
    :height: 2.3cm
    :target: index.html

.. raw:: html

    <center><b>

:ref:`home <home>` - :ref:`about <about>` - :ref:`programmer <programmer>` - :ref:`source <source>` - `pypi <http://pypi.org/project/opbot>`_ - `github <http://github.com/bthate/opbot>`_

.. raw:: html

   </b>
   </center>

'''
autosummary_generate = True
autodoc_default_flags = [
                         'members',
                         'undoc-members',
                         'private-members',
                         'imported-members']
autodoc_member_order = 'bysource'
autodoc_docstring_signature = False
autoclass_content = 'class'
doctest_global_setup = ''
doctest_global_cleanup = ''
doctest_test_doctest_blocks = 'default'
trim_doctest_flags = True
doctest_flags = doctest.REPORT_UDIFF
intersphinx_mapping = {
                       'python': ('https://docs.python.org/3', 'objects.inv'),
                       'sphinx': ('http://sphinx.pocoo.org/', None),
                      }
intersphinx_cache_limit = 1
