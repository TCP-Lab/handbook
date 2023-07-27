---
title: "Structuring Bioinformatics Projects"
weight: 1
desc: "How to structure the filesystem of a bioinformatics project."
---

# Structuring Bioinformatics Projects
*How to structure the filesystem of a bioinformatics project.*

![Ongoing](https://img.shields.io/badge/status-draft-red)

{{< hint warning >}}
This page is still a draft because I'm still writing it.
{{< /hint >}}

## Aim
This page aims to describe how to structure - on the filesystem - a bioinformatics project.

{{< hint info >}}
This page is GitHub-centric.
{{< /hint >}}

## Definition of 'project'

Let's start by defining some terms for the scope of this page.
- A '*project*' is any collection of data, code, and documentation regarding a certain topic, most commonly related to a research paper.
- A '*tool*' is some specific program that performs some task.

It can happen that the point of a project is to develop a tool, but it is not always the case. This article covers structuring *projects*, not tools.

## What is contained in a project

By the definition above, as a bioinformatician on a project, you will most commonly deal with:
- Input Data:
  - Raw Data from (wet) colleagues (e.g. images, `.csv`, `.xslx`, text files);
  - Data from remote repositories (usually fetched trough Application Programming Interfaces, APIs);
- Code:
  - Scripts, tools and similar programs that will need to run to produce some output data.
- Output data:
  - Figures (in `.pdf`, `.png`, `.jpg` and more formats);
  - Tables (most often in `.csv` format);
  - Other blob-like output (e.g. complex binary output from some programs);
- An author manuscript:
  - Usually in word format, but occasionally in `LaTeX` format.

The aim of this article is to give you a guide on where to put each and everyone of these files.

## A sample structure

The most basic idea is to track your work with [`git`](https://git-scm.com/) and push it on [GitHub](https://github.com/). Why? Read the [version control](/docs/code/version_control.md) page.

The only problem is now how to keep order in the chaos and structure your `git` repository. A basic template is:
```
.
├── CONTRIBUTING.md
├── [data]
├── Dockerfile
├── LICENSE
├── makefile
├── [paper]
├── README.md
└── [src]
```
Entries with surrounding brackets (`[]`) are directories. The files are:
- `CONTRIBUTING.md`: Has information on how to contribute to the project. Can be omitted while the project is private, but you could use it to write how other authors can work on the analysis.
- `Dockerfile`: For reproducibility, you will probably make a `Dockerfile`. It should live here, at the root of the repository.
- `LICENSE`: [Choose a license](https://choosealicense.com/). The [MIT](https://choosealicense.com/licenses/mit/) or the [GNU General Public License](https://choosealicense.com/licenses/gpl-3.0/) (GNU-GpL) are good default options. Read [the Turing way chapter on Licensing](https://the-turing-way.netlify.app/reproducible-research/licensing.html) for a primer on why you have to choose a license.
- `makefile`: Read [using makefiles](/docs/project_structure/using_make.md) on why you may want to use a makefile.
- `README.md`: This will be displayed on the landing page of the project. Use it to define:
  - The aim of the project;
  - How to reproduce it;
  - How to contribute (a link to `CONTRIBUTING.md` usually);
  - How to reference your project (does it have a linked publication? Is it published on Zenodo?)
  - Optionally, include *who* contributed to the project in the readme. A way to do this is with the [all contributors bot](https://allcontributors.org/).

We will take a look at the directories more in detail.

### data/
The `data` directory contains the data for the project.
Data can be broadly split in *input*, *intermediate* and *output* data.
I like to think of an extra '*volatile*' type of data, that is required by programs at runtime but can be deleted when the run is over.

We can structure `data/` to follow this mental schema:
- `data/in` contains input data;
- `data/out` contains output data, that should be preserved and potentially exported as output of the project;
  - We can further subdivide `data/out/` in `data/out/figures/` for output figures and store everything else in `data/out` proper.
- `data/` will contain intermediate files that should not be deleted between runs.

Volatile data can be stored in a temporary directory in `/tmp/`, since we do not care for its preservation on disk.

The only issue is with size. Some analyses may use a ton of data, so you cannot store it in the repository directly (see [here]() for GitHub's storage limits).
If you are given large data, an option is to store it remotely, and download it on demand.
For instance, uploading your data to [Zenodo](https://zenodo.org/) and downloading it on the fly on each machine makes your analysis both portable and highly reproducible.
If you also make your data [FAIR](https://www.go-fair.org/fair-principles/), you get extra points, and the world will thank you.

### src/
The 'source' or `src` directory contains code. It should contain *only* code, and nothing else.
The structure of `src` is highly dependent on the project, but in general, try to split 'blocks' of code in intuitive modules. For example, you may have a folder for data wrangling and preprocessing, one for statistical analysis, one for the generation of figures, etc...

If you find that a module is turning - or could be turned - into a proper tool, it is often a good idea to move it out of the repository into its own space, and pull it back as a dependency.

### paper/
You may want to achieve chad-level reproducibility by including your latex code in the repository, next to the analysis proper. You can do this by including a `paper/` folder where you store your paper code.
