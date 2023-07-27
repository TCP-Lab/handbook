---
title: "Python CLI Tools"
weight: 1
desc: "How to (quickly) write neat, clean command line tools in Python."
---

# Making Python command-line tools
*How to (quickly) write neat, clean command line tools in Python.*

![Ongoing](https://img.shields.io/badge/status-draft-red)

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
- The end user has to have Python, of your supported version(s), installed. Take care that Ubuntu users (which are a lot of users) have easy access to an old version of python since Ubuntu takes a long time to update its python binaries. Try to support versions of python that Ubuntu users have access to. You can find this information [here](https://packages.ubuntu.com/search?keywords=python3) for the supported versions of Ubuntu.
- You will need to add Python into any [Docker containers](/handbook/containerizing.md) that you generate that use the tool.
- There is no (easy) way to auto-update a Python CLT.
- Do you need to use an external tool to make your python tool work? If so, search if there is a version of your external tool written as a Python module, or something similar. If there is not, remember that `pip` cannot install it by itself.
  - [`Anaconda`](https://www.anaconda.com/) avoids this by installing the external dependencies itself, but by default injects code in your configurations files and is generally very bulky. Do not use `Anaconda`. If you really *must* use it, use [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) instead.

If this is fine for you, go ahead! If it's not, you probably want a compiled tool. While in theory some python packages claim to produce an executable, this is not the case. Avoid them. Look to natively compiled languages, like Rust or C/C++.

## What development tools do you need?

- Do you need testing? You probably do. You definitely do. But you might not want to due to laziness, a strict time frame, or something else. The standard module to do this is `unittest`, but a large number of projects use `pytest`.
  - I recommend the use of [`pytest`](https://docs.pytest.org/en/latest/).
  - Read the handbook page for [things to keep in mind when writing python code](/handbook/code/python/python_tools.md).
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
- [`pip`](https://pip.pypa.io/en/stable/) to install dependencies;
- [`bump2version`](https://github.com/c4urself/bump2version), a tool that allows you to release a new package version with just one command;
- [`pre-commit`](https://pre-commit.com/) installed and ready to use, to run checks and apply code style before every commit;
- Some [`Github Actions`](https://github.com/features/actions) to run basic testing and CI:
  - An action for tests on pull requests/commits;
  - An action for deployment on release.
- A build system like [`setuptools`](https://setuptools.readthedocs.io/en/latest/) or [`poetry`](https://python-poetry.org/) to build the package;
  - In practice, you install [`build`](https://pypi.org/project/build/) and [`twine`](https://pypi.org/project/twine/) to build and upload the package to PyPI. You will specify which build system to use in the `pyproject.toml` file.
  - I recommend `setuptools` for most packages.

A configurable cookiecutter for this templates is coming soon (tm).

# Part 3 - Write the code
A good thing about python tools is that [`python packages have a predetermined structure`](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

Read the tutorial of your build backend to have an overview of what you have to specify to package your tool.
Most backends will allow to specify to `pip` that the tool has to be installed as a command-line tool.
For example, `setuptools` allows you to set the `entry_points` parameter in the `setup.cfg` file:
```ini
[options.entry_points]
console_scripts =
    executable-name = my_package.module:function
```
At installation time, this tells `pip` to make an executable called `executable-name` that will run the function `my_package.module:function`.

Remember that you can test out the installation of your tool by installing it in a virtual environment with `pip install -e .` in the root folder of your project. Note that this is not the same as installing it with `pip install .`, as the `-e` flag tells `pip` to install the package in "editable" mode, meaning that it will be installed as a symlink to the source code, and any changes to the source code will be reflected in the installed package. This is very useful for development, but also means that packaging caveats, for example the inclusion of local files, might behave differently when installing in editable mode.
If you want to be extra sure that everything works as intended when installing remotely, make a new virtual environment, build the package and install it with `pip install <path to wheel>`.
This will install the package normally, with all the caveats that come with it.

You need to have your tool executed by a single entrypoint, the `my_packages.module:function` part above. For instance, you might have a `my_package` folder with a `__main__.py` file that contains the following:
```python
def main():
    print("Hello world!")
```

You can then specify the entrypoint as `my_package:main`. This will allow you to run the tool as `executable-name` from the command line:
```bash
$ executable-name
Hello world!
```

The logic to run the tool should be in a separate module, so that you can import it and use it in your tests. For this reason, `main` should contain just the logic to parse the command line arguments and call the tool proper.

For example, create a file `main.py` (not `__main__.py`), and add the following:
```python
import argparse

from my_package import my_tool

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file")
    parser.add_argument("output", help="Output file")
    args = parser.parse_args()

    my_tool(args.input, args.output)
```

Then, you can just import `main` in `__main__.py` and call it:
```python
from my_package import main

main()
```
And add to `setup.cfg`:
```ini
[options.entry_points]
console_scripts =
    executable-name = my_package.main:main
```

This way, you can call your package both an `python -m my_package` and `executable-name`. Plus, now `my_tool` is a function that you can import and use in your tests, and `main` is just a thin wrapper around it, parsing the command line arguments.

# Part 4 - Deploy

Once you have written the code, you need to deploy it. This means:
- Build the package with `build`: `python -m build .`;
- Upload it to PyPI with `twine`: `python -m twine upload dist/*`.

And that's it! Remember that if you are still unsure about the quality of your tool, you can always install it directly from GitHub with `pip install git+<GITHUB REPO URL>` instead of uploading it to PyPI. It's a good way to let your colleagues test it before you release it to the world.

You may also use Docker or other containerizing frameworks to deploy your tool. This is a good idea if your tool is complex and has a lot of dependencies, or if you want to make sure that it runs in a very reproducible way. If your tool is relatively small, I would not recommend it.

Finally, think about how you want to track on which release you are at.
You can use [Semantic Versioning](https://semver.org/), or just increment the version number (`v1`, `v2`, `v3` etc...).
In any case, you can use [`bump2version`](https://github.com/c4urself/bump2version) to help updating the version number in the code and in the `setup.cfg` file with just a single command. Read the documentation to learn more.

> There is a [version control](/docs/code/version_control.md) section in the handbook that you might want to read.

# Part 5 - Documentation
Documentation is key. Without it, your tool is useless, as nobody will be able to understand how to use it.

Specify in the `README.md` file how to install and use the tool. If the tool is complex, you might want to use a wiki or a documentation website, like [ReadTheDocs](https://readthedocs.org/) or [GitHub Pages](https://pages.github.com/) to better organize your documentation.
You can set up a GitHub Action to automatically build and deploy the documentation on every commit, so that it is always up-to-date.

Carefully document what the tool wants in input, what it produces as output, and all of its options.
Detail every execution caveat, where logs are stored, and how to ask for help if something goes wrong.

# Part 6 - License
[Choose a license](https://choosealicense.com/). I recommend the MIT license. You, as author, have the freedom to choose the license you want, but remember that if you want your tool to be used by others, you should choose a permissive license. Choose a license has a handy questionnaire that will help you choose the license that best fits your needs.

A project without a license cannot be reused by others. If you do not specify a license, you are implicitly saying that you do not want others to use your code. This is probably not what you want.

> You can read about code licenses in the [FAIR code](/docs/code/fair_code.md) section of the handbook.
