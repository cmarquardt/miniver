# Miniver2
[![license: CC0-1.0](https://img.shields.io/pypi/l/miniver.svg)][cc0]

**Like [versioneer][versioneer], but smaller**

[Miniver][miniver] is a **mini**mal **ver**sioning tool that serves the same purpose
as [Versioneer][versioneer], except that it is not designed to be
cross platform, and only works with Git.

Miniver2 is a friendly fork of Miniver, adding compatibility with Python2.
It's purpose is to give legacy Python2 projects the benefits of Miniver, and to
support their migration to Python3.

#### Why would I use this?
If you are developing a Python package inside a Git repository and
want to get the version directly from Git tags, rather than hard-coding
version strings everywhere.

This is the same problem that Versioneer solves, but Miniver (and Miniver2) is less
than 200 lines of code, whereas Versioneer is over 2000. The tradeoff
is that Miniver only works with Git.

Miniver2 has been tested across Linux as well as macOS X (using Homebrew for
Python); and with both Python 2.7 and 3.6.


[versioneer]: https://github.com/warner/python-versioneer
[miniver]: https://github.com/jbweston/miniver
[cc0]: http://creativecommons.org/publicdomain/zero/1.0/
[pypi]: https://pypi.org/project/miniver/

## Usage
The simplest way to use Miniver2 is to run the following in your project root:
```
curl https://raw.githubusercontent.com/cmarquardt/miniver2/master/install-miniver | python - <your_package_directory>
```
This will grab the latest files from GitHub and set up Miniver2 for your project.

### I get an `unknown` version!
The version is reported as `unknown` (plus the current git hash) when there are no valid tags
in the git history. You should create an [*annotated tag*](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
so that Miniver reports a reasonable version.

If your project uses *unannotated tags* for versioning (though this is not the
[recommended way](https://stackoverflow.com/questions/11514075/what-is-the-difference-between-an-annotated-and-unannotated-tag))
then you'll need to run the following in order to modify Miniver2's behaviour:
```
curl https://raw.githubusercontent.com/cmarquardt/miniver2/master/unannotated-tags.patch | patch <your_package_directory>/_version.py
```

### I don't want to type that URL every time I use this
You can clone (or download a `.zip` containing) this repository and run
`python setup.py install`, which will give you the `install-miniver` script.
Then you can simply run the following from your project root to use Miniver:
```
install-miniver <your_package_directory>
```
Note that other than Miniver, Miniver2 is currently not available via PyPI.

### Can I use this without executing random code from the internet?
Sure! Copy `miniver/_version.py` and `miniver/_static_version.py` from this
repository into your package directory, then copy the following snippets into
the appropriate files:

```python
# Your package's __init__.py
from ._version import __version__
del _version
```

```python
# Your project's setup.py

# Loads _version.py module without importing the whole package.
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


version, ver_cmdclass = get_version_and_cmdclass('mylibrary')

setup(
    name = 'my_package',
    version = version,
    cmdclass = cmdclass,
)
```

```
# Your project's .gitattributes
my_package/_static_version.py export-subst
```

replacing `'my_package'` in the above with the name of your package
(this should be the same as the name of the directory into
which you copied the contents of `miniver`).

That's it!

## License
Miniver and Miniver2 are in the public domain under a CC0 license.
