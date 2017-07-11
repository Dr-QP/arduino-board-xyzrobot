#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv
    brew install cmake || true

    # brew tap caskroom/versions
    brew cask install arduino

    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi

    pyenv install 2.7.10
    pyenv virtualenv 2.7.10 conan
    pyenv rehash
    pyenv activate conan
fi

# pip install conan --upgrade
# pip install conan_package_tools

git clone git@github.com:anton-matosov/conan.git $TMP/conan
git clone git@github.com:conan-io/conan-package-tools.git $TMP/conan-package-tools

BASEDIR=$(dirname "$0")
export PYTHONPATH="$TMP/conan:$TMP/conan-package-tools" $PYTHONPATH

echo """
#!/usr/bin/env python

import sys
sys.path.append('$TMP/conan')  # EDIT!!

from conans.conan import main
main(sys.argv[1:])
""" > /usr/local/bin/conan

conan user

