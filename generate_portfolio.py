import yaml
import os
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open("portfolio_data.yaml", "r",encoding="utf-8") as file:
    data = yaml.safe_load(file)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))
templates = ["index.html", "experience.html", "education.html", "certifications.html", "contactme.html"]

# Ensure docs directory exists
output_dir = "portfolio"
os.makedirs(output_dir, exist_ok=True)

for template_name in templates:
    template = env.get_template(template_name)
    rendered_html = template.render(data)

    # Save index.html at root, others inside docs/
    output_path = template_name if template_name == "index.html" else f"{output_dir}/{template_name}"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

print("Portfolio generated successfully!")
