import sys
import versioneer

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Only install pytest and runner when test command is run
# This makes work easier for offline installs or low bandwidth machines
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    name='tableauserverclient',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Tableau',
    author_email='github@tableau.com',
    url='https://github.com/tableau/server-client-python',
    packages=['tableauserverclient', 'tableauserverclient.models', 'tableauserverclient.server',
              'tableauserverclient.server.endpoint'],
    license='MIT',
    description='A Python module for working with the Tableau Server REST API.',
    test_suite='test',
    setup_requires=pytest_runner,
    install_requires=[
        'requests>=2.11,<3.0',
        'urllib3==1.24.3'
    ],
    tests_require=[
        'requests-mock>=1.0,<2.0',
        'pytest'
    ]
)
