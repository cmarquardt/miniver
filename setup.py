# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys


# Loads version.py module without importing the whole package.
def get_version_and_cmdclass(package_name):
    try: # Python 3
        from importlib.util import module_from_spec, spec_from_file_location
        spec = spec_from_file_location('version',
                                       os.path.join(package_name, "_version.py"))
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.__version__, module.cmdclass
    except: # Python 2
        import imp
        module = imp.load_source(package_name.split('.')[-1],
                                 os.path.join(package_name, "_version.py"))
        return module.__version__, module.cmdclass


version, cmdclass = get_version_and_cmdclass('miniver2')


setup(
    name='miniver2',
    description='minimal versioning tool',
    version=version,
    url='https://github.com/cmarquardt/miniver2',
    author='Christian Marquardt (original: Joseph Weston and Christoph Groth)',
    author_email='christian@marquardt.sc',
    license='CC0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Topic :: Software Development :: Version Control :: Git',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    packages=find_packages('.'),
    cmdclass=cmdclass,
    scripts=['install-miniver2']
)
