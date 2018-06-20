# AWS Lambda Cookiecutter in Python 3.6

This cookiecutter provides a starting point for those wanting to build lambda functions in AWS.

## Prerequisites

* [Python](https://www.python.org/) >= 3.6

## Quickstart

```
# Install cookiecutter
$ pip install cookiecutter

# Generate a new project
$ cookiecutter git@github.com:dbk138/cookiecutter-lambda-python.git

# Follow the prompts to configure your project. See Cookiecutter Options below.

```

## Cookiecutter Options

The following options can be specified when creating a new service.

| Prompt                | Description                                                                                  | Default                        |
| ----------------------| ---------------------------------------------------------------------------------------------| ------------------------------ |
| `project_name`        | A project name synonymous with the git repository name.                                      | New Lambda                     |
| `project_description` | A description of what the project accomplishes.                                              | A new lambda for doing things. | 
| `lambda_name`         | The name of the new lambda.                                                                  | new_lambda                     |
| `lambda_module`       | The name of the Python Lambda module to generate. Must be a Python-compatible identifier.    | new_lambda                     |
| `aws_region`          | The AWS region which you are deploying your lambdas                                          | us-east-1                      |

