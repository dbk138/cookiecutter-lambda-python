# {{cookiecutter.project_name | title()}}

{{cookiecutter.lambda_description}}

## Components

## Testing

## Build and Package

In order to build and deploy our AWS Lambdas we need to zip them up along with all of their dependencies
and store them in a location within S3. Currently we are using Make until a better approach is implemented.
To run Makefiles simply execute the command `make` on the command line. The following are the available make commands:

| Command                       | Description                                                                                                                                     
| ------------------------------| ----------------------------------------------------------------------|
| `make clean`                  | Removes the `dist` directory.                                         |     
| `make {{cookiecutter.lambda_name | replace('_', '-')}}`| Zips up the lambda and places it at the root of the dist directory.   |                      
| `make build`                  | Cleans the dist directory and zips up all lambdas.                    |