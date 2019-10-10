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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Kind2'
copyright = '2019, Board of Trustees of the University of Iowa'
author = 'Cesare Tinelli, Daniel Larraz, Mudathir Mohamed'

# The short X.Y version
version = 'v1.1'
# The full version, including alpha/beta/rc tags
release = 'v1.1.0'

nitpicky = True

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.7.9'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme'
]

# Prefix document path to section labels, otherwise autogenerated labels
# would look like 'heading' rather than 'path/to/file:heading'
# autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    '_build',
    'travis_links.rst'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes',]

# Allow us to modify css as we please
# https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html#overriding-or-replacing-a-theme-s-stylesheet
#
html_style = 'css/styles.css'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Testdoc'

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    # disable fancychap to remove top-level section header styling
    'fncychap': '',
    'fontpkg': r'\usepackage{lmodern}',
    # normally htbp, set to H to prevent floating
    'figure_align':'H',
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        % Uncomment this to remove borders around code blocks
        %   https://stackoverflow.com/a/32910628/8261793   
        %
        %\definecolor{VerbatimBorderColor}{rgb}{1,1,1}

        \usepackage{tocloft}

        % Set smaller fonts for TOC items
        \renewcommand\cftchapfont{\large\bfseries}
        \renewcommand\cftsecfont{\normalsize}

        % Set page numbers to use sans serif as well, size accordingly
        \renewcommand\cftchappagefont{\sffamily\normalsize\bfseries}
        \renewcommand\cftsecpagefont{\sffamily\normalsize}

        % Reduce spacing between TOC items
        \renewcommand\cftchapafterpnum{\vskip-6pt}
        \renewcommand\cftsecafterpnum{\vskip-4pt}


        % Set the width between numbers and chapter headers
        % to be slightly larger, to prevent overlap
        \renewcommand\cftchapnumwidth{1.5em}

        % Indent sections to align with the new chapter titles
        %   https://tex.stackexchange.com/a/50472
        \cftsetindents{section}{2em}{3em}

        % Needed for formatting dates appropriately
        %   https://tex.stackexchange.com/a/212264
        %
        \usepackage{datetime}

        % Change the default sans serif family in the document
        % so that chapter titles can use lmodern
        %   https://tex.stackexchange.com/a/94360
        %
        \renewcommand{\sfdefault}{lmss}
        \renewcommand{\mddefault}{lmss}

        \setcounter{secnumdepth}{2}
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{1}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{titlesec}

        % Removes "Chapter" text and sets the chapter number
        % on the same line as the title
        %   https://tex.stackexchange.com/a/88240
        % 
        \titleformat{\chapter}
            {\sffamily\bfseries\huge}{\thechapter}{20pt}{\huge}

        % Decreases spacing around the chapter titles
        %   https://tex.stackexchange.com/a/63393
        % 
        \titlespacing*{\chapter}{0pt}{-40pt}{20pt}

        \usepackage{color}
        \usepackage{eso-pic}

        \usepackage{setspace}
        \onehalfspacing

        \usepackage{lastpage}
        \usepackage{fancyhdr}
        \usepackage{blindtext}
        \usepackage{xpatch}

       \fancypagestyle{mystyle}{
            \fancyhf{} % clear all header and footer fields
            \fancyfoot[C]{\textbf{\thepage}} % except the center
            \renewcommand{\headrulewidth}{0pt}
            \renewcommand{\footrulewidth}{0pt}
        }
        \xpatchcmd{\chapter}{%
            \thispagestyle{plain}%
        }{%
            \pagestyle{mystyle}
        }{}{}

        % Remove vertical spacing between items in a bulleted list
        % Reduce spacing between paragraphs in an enumerated list,
        % mainly used for the license
        \usepackage{enumitem}
        \setitemize{noitemsep}
        \setenumerate{parsep=2pt}
        \setlist[1]{labelindent=\parindent} % < Usually a good idea

        % Needed in order to get the table of contents to appear on the
        % same page as the title rather than where Sphinx wants to
        % put it. We define this command to be used in maketitle and
        % instead prevent Sphinx from generating the TOC by setting the
        % 'tableofcontents' parameter to be an empty string.
        %   https://tex.stackexchange.com/a/45863
        %
        \makeatletter
        \newcommand*{\toccontents}{\@starttoc{toc}}
        \makeatother

        \sffamily
    ''',
    'sphinxsetup': \
        'verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',
    'extraclassoptions': 'openany,oneside,notitlepage',
    'maketitle': r'''
        \pagenumbering{roman}
        \begin{titlepage}
            \centering

            \vspace*{4mm}

            \sffamily\Large \textbf{\Huge {Kind 2 User Documentation}}

            \sffamily\Large \textbf{Version 1.1.0}

            \newdateformat{monthdayyear}{%
                \monthname[\THEMONTH] \THEDAY, \THEYEAR}
            \monthdayyear\today

            \vspace{4mm}
            \sffamily\toccontents

        \end{titlepage}
        \pagenumbering{arabic}
        ''',
    'tableofcontents': ''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass, toctree_only]).
latex_documents = [
    (master_doc, 'kind2.tex', 'Kind 2 User Documentation', author, 'manual'),
]

latex_docclass = {
    # This causes the header and footers to change, unfortunately
    # 'manual': 'scrbook'
   'manual': 'report'
}

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'kind2', 'Kind 2 User Documentation', [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Test', 'Test Documentation',
     author, 'Test', 'One line description of project.',
     'Miscellaneous'),
]

