#!/bin/bash

set -eo pipefail

if [ -z "${GIT_CURRENT_BRANCH}" ]; then
    GIT_CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
fi

echo "Current branch: ${GIT_CURRENT_BRANCH}"

if [ "${GIT_CURRENT_BRANCH}" = "master" ]; then

    make docs smv=1
    pushd .

    if ! cd docs/build/html; then
        cd docs/build
        cp ../../.ci/index-redirect.html index.html
    else
        cp ../../../.ci/index-redirect.html index.html
    fi

    touch .nojekyll
    tar -czf /tmp/html.tgz .
    popd

    git fetch

    if [ -z $(git branch -a | grep gh-pages) ]; then
        echo "Creating orphan branch gh-pages"
        git checkout --orphan gh-pages
    else
        echo "Checking out existing branch gh-pages"
        git checkout -t origin/gh-pages
    fi

    git rm -rf .
    tar -xvzf /tmp/html.tgz

    for line in $(tar -tf /tmp/html.tgz | grep -E "^\\./." | cut -c3-); do
        echo "${line}"
        git add "${line}"
    done

    git status

    GIT_FILES_ARE_STAGED=$(git diff --cached)

    if [ -n "${GIT_FILES_ARE_STAGED}" ]; then
        git commit -m "Autobuild docs"
        git push origin gh-pages
    else
        echo "Nothing to commit."
    fi

else

    echo "Refusing to build docs since current branch is not master."

fi

git checkout ${GIT_CURRENT_BRANCH} --
