#!/usr/bin/env sh

(
  cd '{{cookiecutter.lambda_module}}' || exit

  echo 'Initializing repository...'
  git init .

  echo 'Setting upstream origin to git@github.com:{{cookiecutter.github_repo}}...'
  git remote add origin 'git@github.com:{{cookiecutter.github_repo}}.git'
)