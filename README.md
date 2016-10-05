# instigitr [![GNU GPL](http://img.shields.io/:license-gpl3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)

instigitr is a python tool for creating git repos and initializing their
README. It also creates a `.gitignore`, which is pulled from a sanitized
list of gitignores provided by GitHub. If the gitignore type is not present
in that list, an empty `.gitignore` is created instead.

## Installation

* run `install.sh` to install to your home directory's `bin` dir.

## Usage

1. create a directory for your new repo: `mkdir my-new-repo`
1. cd into the new directory: `cd my-new-repo`
1. `$ instigitr type` , where `type` is your repo's main language (ex: `C`)

## Contributing

1. Fork it
1. Create your feature branch: `git checkout -b my-new-feature`
1. Commit your changes: `git commit -am 'Add some feature'`
1. Push to the branch: `git push origin my-new-feature`
1. Submit a pull request

## History

* 2016-10-03: initial commit of basic functionality in bash
* 2016-10-04: conversion of basic functionality to Python

## TODO

* Add support for other Licenses (currently only GPL is supported)
* Provide user with choice of repo type rather than relying on them to get
  it right.
* Add support for different types of READMEs (small, med, large, etc)
* Based on the repo type, instantiate the necessary dir structure (this will
  take a while).
