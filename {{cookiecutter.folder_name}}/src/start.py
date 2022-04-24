{% if cookiecutter.use_env== 'y' %}from os import getenv{% endif %}


if __name__ == "__main__":
    print("Project Name: {{cookiecutter.project_name}}")
    print("Hello World!")
