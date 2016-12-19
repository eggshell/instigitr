#!/usr/bin/env python
# Written by Cullen Taylor
# 2016-10-04

import os
import requests
import subprocess
import sys

from jinja2 import Environment, FileSystemLoader
from pick import pick


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


def fetch_all_gitignores():
    subprocess.call(["git", "clone", "git@github.com:github/gitignore",
                     "--depth", "1", "--quiet", "/tmp/gitignore"])
    all_gitignores = [file for file in os.listdir('/tmp/gitignore')
                      if file.endswith(".gitignore")]
    trimmed = [gitignore.replace('.gitignore', '')
               for gitignore in all_gitignores]
    # Give user the option to not select a repo type
    trimmed.append('None')
    return trimmed


def get_gitignore(gitignore_type):
    """Retrieve sane .gitignore from github/gitignore based on user's input
    supplied from the command line.
    """
    ignores_link = 'https://raw.githubusercontent.com/github/gitignore/master/'
    with open('.gitignore', 'a') as curl:
        response = requests.get(ignores_link + gitignore_type +
                                '.gitignore', stream=True)
        if not response.ok:
            touch('.gitignore')
            sys.exit('Not a valid filetype. Wrote empty .gitignore')

        for block in response.iter_content(1024):
            curl.write(block)


def gitignore(gitignore_types):
    """Initialize empty .gitignore if no language/type is supplied
    """
    for gitignore_type in gitignore_types:
        if gitignore_type == 'None':
            touch('.gitignore')
            return
        else:
            get_gitignore(gitignore_type)


def git_init():
    """Run git init on the current directory.
    """
    subprocess.call(["git", "init", "--quiet"])


def handle_choice(choice):
    """Handle user's choice according to their response.
    """
    if choice == 'Yes':
        return
    else:
        sys.exit('Aborted')


def get_choice(choices, title):
    """Function to get a choice from the user. Used to confirm that the user
    wants to make the current directory a git repo, and to get their choice
    of repo type.

    *Arguments:*
    - choices
        - list of choices to present to user
    - title
        - the prompt to present to the user
    """
    choice, index = pick(choices, title)
    return choice


def cleanup():
    """Remove /tmp/gitignore since we don't need it anymore
    """
    subprocess.call(["rm", "-rf", "/tmp/gitignore"])


def instigitr():
    """Executes main functionality of the script. Handles getting a Y/N choice
    from the user, handling it accordingly, initializing the git repo, popu-
    lating the .gitignore, and writing the README.
    """
    choice = get_choice(['Yes', 'No'], 'Do you want to make ' +
                        str(get_current_dir()) + ' a git repo?')
    handle_choice(choice)

    git_init()
    all_gitignores = sorted(fetch_all_gitignores())
    keep_going = True
    gitignore_types = []
    while keep_going:
        gitignore_types.append(get_choice(all_gitignores,
                               'What type of repo are you making?'))
        choice = get_choice(['Yes', 'No'], 'Do you have more types?')
        if choice == 'No':
            keep_going = False

    gitignore(gitignore_types)
    write_readme()
    cleanup()


def main():
    instigitr()
