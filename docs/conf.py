# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

# Add the source directory to the path so Sphinx can find the modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Pipeworks Conditional Axis"
copyright = "2025, aapark"
author = "aapark"
release = "1.0.0"
version = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Auto-generate documentation from docstrings
    "sphinx.ext.napoleon",  # Support for Google-style and NumPy-style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.intersphinx",  # Link to other project documentation
    "sphinx_autodoc_typehints",  # Better type hint rendering
    "myst_parser",  # Markdown support
]

# MyST (Markdown) parser configuration
myst_enable_extensions = [
    "colon_fence",  # ::: for directives
    "deflist",  # Definition lists
    "fieldlist",  # Field lists
    "html_admonition",  # HTML-style admonitions
    "html_image",  # HTML-style images
    "linkify",  # Auto-detect URLs
    "replacements",  # Text replacements
    "smartquotes",  # Smart quotes
    "substitution",  # Variable substitution
    "tasklist",  # Task lists with checkboxes
]

# Source file suffixes
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document
master_doc = "index"

# Suppress warnings for cross-references to files outside the docs tree
# These files (CLAUDE.md, README.md, etc.) are in the repo root and intentionally
# not part of the Sphinx documentation source. The links work on GitHub.
suppress_warnings = [
    "myst.xref_missing",  # Suppress MyST cross-reference warnings
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Theme options
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": True,  # Prevents dynamic reordering
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

# -- Extension configuration -------------------------------------------------

# Autodoc configuration
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Intersphinx configuration (link to other projects)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- Options for different output formats ------------------------------------

# LaTeX/PDF output
latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": "",
    "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files
latex_documents = [
    (
        master_doc,
        "PipeworksConditionalAxis.tex",
        "Pipeworks Conditional Axis Documentation",
        "aapark",
        "manual",
    ),
]

# Manual page output
man_pages = [
    (
        master_doc,
        "pipeworks-conditional-axis",
        "Pipeworks Conditional Axis Documentation",
        [author],
        1,
    )
]

# Texinfo output
texinfo_documents = [
    (
        master_doc,
        "PipeworksConditionalAxis",
        "Pipeworks Conditional Axis Documentation",
        author,
        "PipeworksConditionalAxis",
        "Structured, rule-based framework for generating coherent state descriptions.",
        "Miscellaneous",
    ),
]
