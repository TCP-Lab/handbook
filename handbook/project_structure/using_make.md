# Using GNU Make for rebuilding projects
![Draft](https://img.shields.io/badge/status-draft-red)

> This page is still a draft because I'm still writing it.

## Aim
This page is handy when writing or reading `makefile`s for projects.

## Special variables

GNU make will set special variables in every rule run. See [the official documentation][^gnu_auto_vars]. A very quick primer:
```
|------------ $@ ---------------|
|-- $(@D) ---| |----- $(@F) ----|   |-------- $< -------|
some\path\to\a\very_cool_file.txt : some_prerequisite.csv
```

- `$(@D)` is especially useful to run `mkdir -p $(@D)`;

[gnu_auto_vars]: https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
