"""Package configuration"""

import os


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.2.2"


with open('README.rst') as fp:
    README = fp.read()


with open('HISTORY.rst') as fp:
    HISTORY = fp.read().replace('.. :changelog:', '')


with open(os.path.join('requirements', 'base.in')) as fp:
    REQUIREMENTS = list(fp)


setup(
    name='pip-compile-multi',
    version=VERSION,
    description="Compile multiple requirements files "
                "to lock dependency versions",
    long_description=README + '\n\n' + HISTORY,
    author='Peter Demin',
    author_email='peterdemin@gmail.com',
    url='https://github.com/peterdemin/pip-compile-multi',
    include_package_data=True,
    packages=['pipcompilemulti'],
    install_requires=REQUIREMENTS,
    license="MIT",
    zip_safe=False,
    keywords='pip-compile-multi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'pip-compile-multi = pipcompilemulti.cli_v1:cli',
            'requirements = pipcompilemulti.cli_v2:cli',
        ]
    },
)
