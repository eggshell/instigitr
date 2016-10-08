from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='instigitr',
      py_modules=['instigitr'],
      data_files=[('templates', ['templates/readme.tmpl'])],
      entry_points={'console_scripts': ['instigitr = instigitr:main']},
      version='0.1',
      description='Git repo generator',
      long_description=readme(),
      url='http://github.com/egg-shell/instigitr',
      author='Cullen Taylor',
      author_email='cullentaylor@outlook.com',
      license='GPL',
      include_package_data=True,
      zip_safe=False)
