from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from pathlib import Path
import json

# Setup Jinja2 template environment
env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))

def load_template(name: str):
    try:
        return env.get_template(f"{name}.json")
    except TemplateNotFound:
        raise FileNotFoundError(f"Template '{name}.json' not found.")

def substitute(template, variables: dict) -> dict:
    rendered_str = template.render(**variables)
    return json.loads(rendered_str)