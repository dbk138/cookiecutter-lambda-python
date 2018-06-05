.PHONY: clean build build-{{cookiecutter.lambda_module | lower | replace('_', '-')}}

# Remove the distribution directory
clean:
	rm -rf dist

# Build and package {{cookiecutter.lambda_name}}
build-{{cookiecutter.lambda_name | replace('_', '-')}}:
	mkdir -p dist/{{cookiecutter.lambda_name}}
	zip -r ./dist/{{cookiecutter.lambda_name}}.zip ./{{cookiecutter.lambda_name}}/{{cookiecutter.lambda_name}}.py
	python3 -m venv dist/{{cookiecutter.lambda_name}}
	. dist/{{cookiecutter.lambda_name}}/bin/activate; \
	pip install  -r {{cookiecutter.lambda_name}}/requirements.txt; \
	cp -r $$VIRTUAL_ENV/lib/python3.6/site-packages/ dist/{{cookiecutter.lambda_name}}
	cd dist/{{cookiecutter.lambda_name}}; zip -g -r ../{{cookiecutter.lambda_name}}.zip . -x "*__pycache__*" "*dist-info*" "*include*" "lib*"

build: clean build-{{cookiecutter.lambda_module | replace('_', '-')}}