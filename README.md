# instigitr

[![Build Status](https://travis-ci.org/egg-shell/instigitr.svg?branch=master)](https://travis-ci.org/egg-shell/instigitr)
[![GNU GPL](http://img.shields.io/:license-gpl3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)

instigitr is a command-line tool for creating git repos and initializing their
README. It also creates a `.gitignore`, which is pulled from a sanitized
list of gitignores provided by GitHub.

## Installation

1. Clone this repository to your local machine:

    ```
    git clone git@github.com:egg-shell/instigitr.git
    ```

1. Install the pip package from the repo's root directory:

    ```
    pip install .
    ```

## Usage

Create a directory for your new repo, navigate to it and run `instigitr`:

    mkdir my-new-repo
    cd my-new-repo
    instigitr

## Support

Please use the [issue tracker](https://github.com/egg-shell/instigitr/issues)
for bug reports and feature requests.

## Contributing

Please contribute using
[Github Flow](https://guides.github.com/introduction/flow/).
Create a branch, add commits,
and [open a pull request](https://github.com/egg-shell/instigitr/compare/).

## License

This project is licensed under the GNU GPL License - see the
[LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* Thanks to [wong2/pick](https://github.com/wong2/pick) for the easy-to-use
  user choice API.

