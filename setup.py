#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='DragonTV Plugin',
    version='1.0.1',

    author='Adam Morris',
    author_email='amorris@mistermorris.com',
    license='GPL v3 or later',
    install_requires = [
        'MediaDrop >= 0.11dev', # use whatever version you support
    ],

    include_package_data=True,
    # only necessary if you use namespace packages
    # namespace_packages = ['mediadropext'],
    packages=find_packages(),

    # define the namespaces here    
    entry_points = {
        'mediadrop.plugin': [
            'offcampus = dragontv_plugin.main',
            'another = dragontv_plugin.main2',
        ],
    },

    message_extractors = {'dragontv_plugin': [
        ('templates/**.html', 'genshi', {'template_class': 'genshi.template.markup:MarkupTemplate'}),
    ]},
)
