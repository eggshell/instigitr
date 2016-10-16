# instigitr

[![Build Status](https://travis-ci.org/egg-shell/instigitr.svg?branch=master)](https://travis-ci.org/egg-shell/instigitr)
[![GNU GPL](http://img.shields.io/:license-gpl3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)

instigitr is a python tool for creating git repos and initializing their
README. It also creates a `.gitignore`, which is pulled from a sanitized
list of gitignores provided by GitHub. If the gitignore type is not present
in that list, an empty `.gitignore` is created instead.

## Installation

* `git clone` this repository to your local machine.
* Run `pip install .` from the repo's root directory.

## Usage

1. create a directory for your new repo: `mkdir my-new-repo`
1. cd into the new directory: `cd my-new-repo`
1. `$ instigitr`, and follow the on-screen prompts

## Contributing

1. Fork it
1. Create your feature branch: `git checkout -b my-new-feature`
1. Commit your changes: `git commit -am 'Add some feature'`
1. Push to the branch: `git push origin my-new-feature`
1. Submit a pull request

## History

* 2016-10-03: initial commit of basic functionality in bash
* 2016-10-04: conversion of basic functionality to Python
* 2016-10-06: added ability to install via pip
* 2016-10-15: give users a menu for their choices, eliminating CL args

## TODO

* Add support for other Licenses (currently only GPL is supported)
* Add support for different types of READMEs (small, med, large, etc)
* Based on the repo type, instantiate the necessary dir structure (this will
  take a while).
