# Warning! [![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/tree/main)
**This is an old stale branch for the LaTeX preamble. Please only use this if
you try to compile your old projects. Any problems with this preamble will not
be fixed! Please use the
[main](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/tree/main)
branch for your new projects.**

# LaTeX - Preamble and Examples [![version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/tree/version/main-v1)
This small repository contains a LaTeX Preamble with settings for Computer
Science handins together with a document with examples of use of all the
different packages in the preamble together with a template to get a new
document started quicker.

## Preamble
The preamble is made in two parts, with the intent to divide the settings
between the general and the localization specific settings. This is only of
value, should you write your .tex document in various languages.
- base: Packages and most settings
- dk/en: Settings specifically for localization to danish (dk) or english (en).

When importing the preamble you have to only import the localized .tex file,
since there's already a call to the base settings within both. How you import it
depends on where you have the preamble files located compared to your document.

### Same folder
```tex
\documentclass[a4, english]{article}
\input{preamble_en.tex}
```

### Absolute path
On Windows
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{C:/GitHub/LaTeX_Preamble_and_Examples/preamble/}{preamble_en.tex}
```

On Unix
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{/home/username/Documents/LaTeX_Preamble_and_Examples/preamble/}{preamble_en.tex}
```

### Relative path
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\subimport{../preamble/}{preamble_en.tex}
```

## Documents
This repository contains three documents, _template_report.tex_,
_template_blank.tex_ and _example.tex._
### template_report.tex and template_blank.tex
With *template_report.tex* you have a very small and sparse document, in which
already the preamble, abstract, title, bibliography and two sections are ready
for use. This should get you started much faster. ![Alt
text](/img/template.png?raw=true "The template file")

With *template_blank.tex* you simultaneously have a completely blank document
with nothing more than just the title.

### examples.tex
A slowly growing document with explanations and examples of using the various
packages in the preamble. They are all made with the intent to be reverse
engineerable. ![Alt text](/img/example.png?raw=true "The template file")

## Python Template Generator
In the folder Python you can find a Python Template Generator, created by
Kristian 'Yurippe' Gausel. *prepare.py* is the file that creates *latexgen.py*
and packs the template and the *preamble_en*, *preamble_dk* and *preamble_base*
into *latexgen.py* to create a standalone script to generate a template from

This is especially useful for ShareLatTeX since you can add a --zip argument to
zip the template into a ShareLaTeX compatible format for easy upload.

The *latexgen.py* file can be found under
[Releases](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/releases)
