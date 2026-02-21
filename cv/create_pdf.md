# Instructions

## Install

```
brew install pandoc
brew install --cask mactex
```

## Create PDF

```
pandoc cv/luke_conibear_cv.md -o public/cv/luke_conibear_cv.pdf -V colorlinks=true -V urlcolor=teal -V geometry:margin=0.75in
```
