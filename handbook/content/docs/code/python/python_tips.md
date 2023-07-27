---
# This is the page metadata header. It is written in YAML format
# Full reference: https://github.com/alex-shpak/hugo-book/tree/master#page-configuration
title: "Python Tips" # The page title. Will show up in the index only
weight: 1 # Pages with more weight will show up higher in the index. Pages with the same weight are ordered alphabetically
desc: "Tips and tricks to keep in mind when writing Python code." # The description to be used in the index files.
draft: false # If this is true, the page will not be included in the live site or the indexes.

# Optional:
#bookCollapseSection: true # Will collapse other pages in this section. Useful in _index.md pages
#bookFlatSection: true # Opposite of 'bookCollapseSection', and the default.
#bookTOC: false # Hide the TOC in this page
#bookSearchExclude: true # Hide this page from search results. Useful in _index.md pages.
---

# Python Tips
> Tips and tricks to keep in mind when writing Python code.
![Draft](https://img.shields.io/badge/status-draft-red)

{{< hint warning >}}
This page is still a draft because I'm still writing it.
{{< /hint >}}

## Aim
This page aims to collect every concept useful to keep in mind while writing python: from code style, to documentation, to best practices.

## The tips

- Follow a code style. Automatic formatters like [`black`](https://github.com/psf/black) are your friend. You can have a [pre-commit hook](https://pre-commit.com/) to automatically format your code before committing it. This ensures you are compliant, and you can just forget about it.
  A code style gives you ac consistency in your code, and makes it easier to read. It also makes it easier to collaborate with other people, with less git conflicts.
- Use type hints. They make life so much easier. Some IDEs can even use them to provide autocompletion, and provide a (sort of) static analysis of your code. Read more about them [here](https://docs.python.org/3/library/typing.html).
  Dynamic typing is a mistake, and is [generally frowned upon in most civilized societies](https://www.youtube.com/watch?v=vfewyAHeTYw).
- Write docstrings. They are the best way to document your code. They are also used by some IDEs to provide extra help on autocompletion. Read more about them [here](https://www.python.org/dev/peps/pep-0257/).
  If you write them well, you can use `sphinx` to automagically generate documentation for your code. Read more about it [here](https://www.sphinx-doc.org/en/master/).
- Use `isort` to sort your imports. It is a great tool that can be used as a pre-commit hook. It will sort your imports in a consistent way, and will group them in sections. Read more about it [here](https://pycqa.github.io/isort/). If you also use `black`, use `isort --profile black` to make sure the imports are sorted in the same way as `black` would format them. If you don't, the two tools will fight each other. Read more [here](https://pycqa.github.io/isort/docs/configuration/black_compatibility.html).
  This means more consistent code, and less git conflicts.
