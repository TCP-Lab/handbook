---
title: "Python CLI Tools"
weight: 1
---

# Making Python command-line tools
*How to (quickly) write neat, clean command line tools in Python.*

![Draft](https://img.shields.io/badge/status-draft-red)

{{< hint warning >}}
This page is still a draft because I'm still writing it.
{{< /hint >}}

## Aim
This page aims to describe how to make command-line tools in python, covering how to package, configure and deploy them. It does not aim to cover how to package a python project. See "Also Read" below.

## Also Read
- Python's ["packaging python projects"](https://packaging.python.org/en/latest/tutorials/packaging-projects/) tutorial.

# Part 1 - Define what you need

## Is Python good for you?
A command-line tool (CLT) can be very useful to automate routine tasks. First of all, ask yourself these questions.

Can your CLT be written in bash? If so, do that. See the [bash tools](./bash_tools.md) page for more information. Bash is available virtually everywhere, does not require compilation, and is very portable (you just copy the file).

Python is an easy choice to make when trying to build a more complex CLT, since it's very easy to write, and the package ecosystem is very varied. However, keep in mind that:
- The end user has to have Python, of your required version, installed. Take care that Ubuntu users usually can only access an old version of python (such losers, right?) since Ubuntu takes a long time to update its python binaries. Try to use the lowest version of python that you can.
- You will need to add Python into any [Docker containers](/handbook/containerizing.md) that you generate that use the tool.
- There is no (easy) way to auto-update a Python CLT.
- Do you need to use an external tool to make your python tool work? If so, search if there is a version of your external tool written as a Python module, or something similar. If there is not, remember that `pip` cannot install it by itself.
  - [`Anaconda`](https://www.anaconda.com/) avoids this by installing the external dependencies itself, but literally takes control of your computer while doing so, akin to cancer. Do not use `Anaconda`. If you really *must* use it, use [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) instead.

If this is fine for you, go ahead! If it's not, you probably want a compiled tool. While in theory some python packages claim to produce an executable, this is not the case. Avoid them. Look to natively compiled languages, like Rust or C/C++.

## What development tools do you need?

- Do you need testing? You probably do. You definitely do. But you might not want to due to laziness, a strict time frame, or something else. The standard module to do this is `unittest`, but a large number of projects use `pytest`.
  - I recommend the use of [`pytest`](https://docs.pytest.org/en/latest/).
  - Read the handbook page for [things to keep in mind when writing python code]
- Do you need [Continuous Integration](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration) (CI)? You might not need CI if the tool is small or internal. CI is really useful if the tool is (or might become) very large and complex, or when a lot of contributors will update it, as it forces you to write meaningful tests and keeps the online code clean.
  - GitHub Actions or [Travis](https://www.travis-ci.com/) can be used to do this for free if the project is open source. If it is not, they charge a price.
  - Prefer GitHub Actions over Travis.
- Do you need to deploy to PyPI?
  - If the tool is aimed at a widespread consumption, use PyPI.
  - If the tool is very niche, or you will need to update it very frequently, you can install it directly from GitHub trough `pip`. Do not upload (yet) ot PyPI.
- Do you need extended documentation for your project?
  - If the tool is easy to use, `the README.md` of the project is often enough.
  - If the tool is really complex, you might want to use (in order of complexity) [Github Wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis), [GitHub Pages](https://pages.github.com/) or [ReadTheDocs](https://readthedocs.org/). I recommend Github Wikis or Read The Docs.

# Part 2 - Cookiecut

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a python tool that generates projects based on templates, or cookiecutters (CCs).

There are a lot of python cookiecutters around. See for instance [this github search](https://github.com/search?q=cookiecutter+python+tool&type=repositories) resulting in ~50 CCs for "Python tool".

A **lot** of these CCs are very bloated: they cram in as many tools as they can to be "cool". Do not be cool.
Depending on what you answered above, you probably need:
- [`pdm`](https://github.com/pdm-project/pdm): A substitute for `pip`, `pdm` manages the dependencies of the tool, and follows Python's PEP standards. It also builds your project's wheels.
- [`bump2version`](https://github.com/c4urself/bump2version), a tool that allows you to release a new package version with just one command;
- [`pre-commit`](https://pre-commit.com/) installed and ready to use, to run checks and apply code style before every commit;
- Some [`Github Actions`](https://github.com/features/actions) to run basic testing and CI:
  - An action for tests on pull requests/commits;
  - An action for deployment on release.

A configurable cookiecutter for this templates is coming soon (tm).

# Part 3 - Write the code


# Part 4 - Deploy

