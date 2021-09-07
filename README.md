# Differenpy

[![Github CI](https://github.com/notabu/python-project-lvl2/actions/workflows/ci.yml/badge.svg)](https://github.com/notabu/python-project-lvl2/actions/workflows/ci.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/80babc02ce31b73413bf/maintainability)](https://codeclimate.com/github/notabu/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/80babc02ce31b73413bf/test_coverage)](https://codeclimate.com/github/notabu/python-project-lvl2/test_coverage)


A difference calculator is a program that determines the difference between two data structures. This is a popular task, for which there are many online services http://www.jsondiff.com/. Such a mechanism, for example, is used in the output of tests or in the automatic tracking of changes in configuration files.

## Installation

Clone the repo and install packages
```sh
git clone git@github.com:znhv/differenpy.git

cd defferenpy
   
make install
```
   
## Usage

```shell
$ gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```

## License
[MIT](https://github.com/znhv/differenpy/blob/main/LICENSE)