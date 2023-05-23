![Ongoing](https://img.shields.io/badge/status-ongoing-orange)

If you're reading this you are either a CMA-Lab member or someone from the Internet. If you're the latter, welcome! Thanks for taking a look at the handbook. If you want to contribute, you found an error or would simply like to suggest an edit, [open an issue](https://github.com/CMA-Lab/Handbook/issues) or reach out by [sending us an email](mailto:luca.visentin@unito.it).

If you like the handbook, drop a star! It really helps with my mental health.

# Contributing
We welcome any and all contributions!

This might be your first time contributing to something on GitHub. Don't worry, it's simpler that it looks. You can follow one of the many - many - guides online, such as:
- [The basics of Git in 10 minutes](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/) by freecodecamp.
- GitHub's own [quickstart guide](https://docs.github.com/en/get-started/quickstart/hello-world), especially the section on [contributing to a project](https://docs.github.com/en/get-started/quickstart/contributing-to-projects);
- Try to contribute to [this project](https://github.com/firstcontributions/first-contributions) to actually do a first contribution and see how it's done.

## Pre-commit
A pre-commit hook is available to regenerate the index files when you commit, so
you don't have to do it manually. Just follow these easy steps to set it up:
- Install [Python](https://www.python.org/) and be sure that you can call the `python` and `pip` commands from the command line (i.e. that they are in your `PATH`);
- Install [pre-commit](https://pre-commit.com/#install), usually just `pip install pre-commit` (i suggest installing it *outside* a virtual environment);
- `cd` into the repository root (where the `.pre-commit-config.yaml`) file is;
- Run `pre-commit install`.
- You're done!

When you commit, pre-commit will run, and update the indexes as needed. If it needs to update some files, it will abort the commit (so you can inspect what it did). It is (usually) safe to run `git add . && !!` to add all changes and commit again - the pre-commit will run again, change no file, and allow you to commit the updated files.

More information [can be found in the pre-commit documentation](https://pre-commit.com/#usage).

## Recognizing contributions
If you contributed to the handbook, you'll be credited at the bottom of the main [README.md](README.md) file. If you contributed but you're not included, [open an issue](https://github.com/CMA-Lab/Handbook/issues) - feel free to scold us.

If you want to contribute, you must follow [CMA-Lab's code of conduct](https://github.com/CMA-Lab/.github/blob/main/CODE_OF_CONDUCT.md).

# Using the handbook
The handbook is mainly targeted at people in CMA-Lab, but it is open source and fully accessible, copy-pastable, and usable by anyone. We are licensed under the permissive [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. All standalone code in the book is licensed under the [MIT license](https://opensource.org/license/mit/), you can do basically what you want to do with it, but do give us credit.

## Citing the handbook
If you ever need (or want) to cite us, use the following DOI:

> COMING SOON!

# Writing the handbook
The handbook is written in GitHub-flavoured Markdown:
- [Markdown basics for the non-believers](https://www.markdownguide.org/basic-syntax/)
- [Github's guide on its own markdown format](https://github.github.com/gfm/#what-is-github-flavored-markdown-)

Note that Github's markdown is used everywhere - in `.md` files, in comments, issues, pull requests, etc...

Links are written as `[link text](link)`. Links to pages in the handbook can be given relative to the current file (`handbook/README.md`) or absolute (`/CONTRIBUTING.md`, note the starting `/`). Github handles making them point to the correct files in the correct branches.

In triple-backtick code blocks, remember to specify the language of your code block to allow for the correct syntax highlighting. See [this guide](https://github.com/jincheng9/markdown_supported_languages) to see a list of supported languages.

You can also start code blocks by prepending each line by *eight* spaces. Why? I have no idea, but it makes code blocks possible in bullet points. To annotate the language of the eight-spaces-indented code you can use this template:
```md
- This is a bullet point.

    <!-- language: language-tag -->
        code goes here
        and here's another line

- This is the next bullet point.
```
This renders as:
- This is a bullet point.

    <!-- language: md -->
        code goes here
        and here's another line

- This is the next bullet point.

Remember that markdown is converted to HTML for rendering. So you can actually write most HTML code in markdown and it will be rendered correctly. This is essential when adding images or GIFs. Use `<img><\img>` tags to include your images. GitHub does not like large images in repositories, so upload them to some third-party host and add a link to the raw image for now.

## What to write in the handbook

This handbook does not want to be a copy-paste of other - probably better - guides on the internet. It is a place to store and iterate upon best practices, standardized processes and more, mainly aimed at the CMA-Lab members. A meta-science "guide" of sorts. For this reason, do not simply copy-and-paste things you find on the internet - link to them instead.

There is a general template for new pages. You can copy-paste it from [the page template file](TEMPLATE.md) and fill in the blanks.

## How to write the handbook

The handbook is made up of several **pages**. Each page has its own `.md` file.
The `handbook` folder is the start of the handbook. The `README.md` of that folder contains the index of the handbook.
Every subfolder in `handbook/` is a **binder**. Binders bind bound pages, grouping them in topics. The `README.md` for each binder contains the topic and a binder-specific index.

Each page in the handbook **MUST** follow the structure in the [`TEMPLATE.md`](TEMPLATE.md) file in the root of the repository. This is needed to automatically regenerate the index files around the folders with the new pages.

### Rule 1 - Keep it simple, stupid
If you are writing a page in the handbook, keep it simple and concise. Include links to external resources if possible but always describe why the link is there - remember that this is not a wiki.

Love bullet points and avoid long and boring sentences. Keep your language as accessible as possible. If a concept is hard but an explanation of it does not fit in the theme of the page, move it to its own page.

The fact that you need to KISS does not mean being unclear or imprecise for the sake of conciseness. The final aim of the handbook is to be useful - make it so.

Do **not** use or reuse acronyms without defining them first. Use them sparingly.

### Rule 2 - Remember where you are at
If you are drafting a brand-new page, include at the top of the page the status of the page with a meaningful shields.io badge:

- If the page is completed, or in general will require little further editing to be complete: ![Complete](https://img.shields.io/badge/status-complete-brightgreen) ( `![Complete](https://img.shields.io/badge/status-complete-brightgreen)` )
- If the page is an ongoing effort but it is still usable: ![Ongoing](https://img.shields.io/badge/status-ongoing-orange) (`![Ongoing](https://img.shields.io/badge/status-ongoing-orange)`)
- If the page is a draft, and still requires a lot of work, or is unusable in general, use: ![Draft](https://img.shields.io/badge/status-draft-red) ( `![Draft](https://img.shields.io/badge/status-draft-red)` ). Do not add draft pages to the index.

If you're drafting, a link to the relevant drafting issue(s) (if any) is also useful. Disclaimers on top of the page (within quote blocks maybe) are also useful:

> NOTICE: Your noticing of this notice was noted.

### Rule 3 - Be opinionated
Do not worry about being opinionated. This is **the** place to have opinions. You know that a tool is better that another? Suggest its use. You think that a popular workflow sucks? Say so, and propose alternatives.

If you do not agree with something that is written in the handbook, [open an issue](https://github.com/CMA-Lab/Handbook/issues) and say your take on it. This is how we grow and develop the handbook.

### Rule 4 - There's only fun here
This handbook should be useful, correct and concise, but there is no need to be overly formal. Keep those for boring people and meetings.

You can, and should, use emojis (copy-paste them) and gifs when appropriate (which means basically anywhere you like).

# Make it so
Now go, write the handbook, and make it so.
<p align="center">
<img src="https://media4.giphy.com/media/bKnEnd65zqxfq/giphy.gif?cid=ecf05e472pjf47sr39yxkr11k56dwsczxkai5ucxndguzl3a&ep=v1_gifs_search&rid=giphy.gif&ct=g" width = 500 align="center">
</p>
