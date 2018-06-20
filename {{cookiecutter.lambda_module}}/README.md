# {{cookiecutter.project_name | title()}}

{{cookiecutter.lambda_description}}

## Requirements

* [Python](https://www.python.org/) >= 3.6
* [NPM](https://www.npmjs.com/get-npm) - for installing serverless.
* [Serverless](https://serverless.com/) - for deploying to AWS.
* AWS Account and Credentials

## Components

## Testing

## Build, Package, and Deploy

In order to build and deploy our AWS Lambdas we need to zip them up along with all of their dependencies. 
[Serverless](https://serverless.com/) allows us to accomplish that with ease. It can easily be swapped out for 
another approach. The following are the available commands:

| Command                       | Description                                                                                                                                     
| ------------------------------| ----------------------------------------------------------------------|
| `serverless deploy`           | Deploy the lambdas that you've created                                |     