# -*- coding: utf-8 -*-

"""invenio3 Invenio instance."""

import os

from setuptools import find_packages, setup

# Get the version string. Cannot be done with import!
version = {}
with open(os.path.join('invenio3', 'version.py'), 'rt') as fp:
    exec(fp.read(), version)

setup(
    name='invenio3',
    version=version['__version__'],
    description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'invenio3 = invenio3.cli:cli'
        ],
        'invenio_workflows.workflows': [
            'MyWorkflow = invenio3.workflows:MyWorkflow',
            'MyRecordWorkflow = invenio3.workflows:MyRecordWorkflow'
        ],
        'invenio_workflows_ui.actions': [
            'Approval = invenio3.actions:Approval'
        ],
        'invenio_assets.bundles': [
            'invenio3_ui_js = invenio3.bundles:js'
        ],
        'invenio_search.mappings': [
            'holdingpen = invenio3.mappings'
        ],
        'invenio_base.blueprints': [
            'invenio3_main = invenio3.views:blueprint'
        ],
    },
    install_requires=[
        'invenio-base>=1.0.0a3',
    ],
)
