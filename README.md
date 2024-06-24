# executable

Create windows .exe files that just wrap a Python script.

## Installation

```bash
pip install executable
```

## Usage

```console
$ cat .\hello.py
print("Hello!")

$ executable .\hello.py
Created .\out\hello.exe and .\out\hello-script.py

$ ./out/hello
Hello!

$ executable .\hello.py --create-cmd
Created .\out\hello.cmd and .\out\hello-script.py

$ .\out\hello
Hello!
```

## Local Development / Testing

- Create and activate a virtual environment
- Run `pip install -r requirements-dev.txt` to do an editable install
- Run `pytest` to run tests

## Type Checking

Run `mypy .`

## Create and upload a package to PyPI

Make sure to bump the version in `setup.cfg`.

Then run the following commands:

```bash
rm -rf build dist
python setup.py sdist bdist_wheel
```

Then upload it to PyPI using [twine](https://twine.readthedocs.io/en/latest/#installation):

```bash
twine upload dist/*
```
