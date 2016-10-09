#!/usr/bin/env python
# Written by Cullen Taylor
# 2016-10-04

import os
import requests
import subprocess
import sys

from jinja2 import Environment, FileSystemLoader


def get_script_path():
    """Returns path where instigitr actually lives. ex:
       ${HOME}/username/.virtualenvs/instigitr/libs/python-2.7/site-packages
    """
    return os.path.dirname(os.path.split(os.path.realpath(sys.argv[0]))[0])


def get_current_dir():
    """Returns directory where user called instigitr
    """
    return os.path.split(os.getcwd())[1]


def generate_readme(template_file):
    """Generate readme from template using jinja2
    """
    print get_script_path()
    template_loader = FileSystemLoader(searchpath=(get_script_path() +
                                                   '/templates'))
    template_env = Environment(loader=template_loader)
    template = template_env.get_template(template_file)
    template_vars = {"title": get_current_dir()}
    output = template.render(template_vars)
    return output

def write_readme():
    """Writes readme that is generated from template
    """
    readme = generate_readme('readme.tmpl')
    with open('README.md', 'wb') as file:
        file.write(readme)


def touch(fname, times=None):
    """Essentially run GNU coreutils' touch
    """
    with open(fname, 'a'):
        os.utime(fname, times)


def get_gitignore(repo_type):
    """Retrieve sane .gitignore from github/gitignore based on user's input
    supplied from the command line.
    """
    ignores_link = 'https://raw.githubusercontent.com/github/gitignore/master/'
    with open('.gitignore', 'wb') as curl:
        response = requests.get(ignores_link + repo_type +
                                '.gitignore', stream=True)
        if not response.ok:
            touch('.gitignore')
            sys.exit('Not a valid filetype. Wrote empty .gitignore')

        for block in response.iter_content(1024):
            curl.write(block)


def gitignore(repo_type):
    """Initialize empty .gitignore if no language/type is supplied
    """
    if repo_type is None:
        touch('.gitignore')
        return
    else:
        get_gitignore(repo_type)


def git_init():
    """Run git init on the current directory.
    """
    subprocess.call(["git", "init"])


def handle_choice(choice):
    """Handle user's choice according to their response.
    """
    if choice is True:
        return
    else:
        sys.exit('Aborted')


def get_choice(current_dir):
    """Function to get Y/N decision from user. If the answer is affirmative,
    the current dir will be initialized. If the answer is negative, instigitr
    will exit.

    *Arguments:*
    - current_dir
        - name of current directory, where user executed instigitr. obtained
          by get_current_dir()
    """
    yes = set(['yes', 'ye', 'y', ''])
    no = set(['no', 'n'])

    print("Do you want to make %s a git repo? [Y/N]" % current_dir)
    while True:
        choice = raw_input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            sys.stdout.write("Please respond with 'yes' or 'no': ")


def instigitr(repo_type):
    """Executes main functionality of the script. Handles getting a Y/N choice
    from the user, handling it accordingly, initializing the git repo, popu-
    lating the .gitignore, and writing the README.

    *Arguments:*
    - argv
        - list of command line arguments passed to instigitr.
    """
    choice = get_choice(get_current_dir())
    handle_choice(choice)

    git_init()
    if repo_type is None:
        gitignore(None)
    else:
        gitignore(repo_type)

    write_readme()

def main():
    instigitr(sys.argv[1])
