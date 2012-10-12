import os
import sys

reload(sys).setdefaultencoding("UTF-8")

from setuptools import setup, find_packages


def read(*pathnames):
    return open(os.path.join(os.path.dirname(__file__), *pathnames)).read().\
           decode('utf-8')

version = '1.0-rc1'

setup(name='plone.formwidget.countingtextarea',
      version=version,
      description="A counting textarea for z3cform to be used for dexterity schemas.",
      long_description='\n'.join([
          read('README.rst'),
          read('CHANGES.rst'),
          ]),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='plone countingtextarea dexterity z3cform',
      author='Bo Simonsen',
      author_email='bo@headnet.dk',
      license="GPLv2+",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.supermodel',
          'plone.app.registry',
      ],
      extras_require = {
          'test': [
              'plone.testing',
              'plone.app.testing',
              ]
          },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
