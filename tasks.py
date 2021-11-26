import os
from invoke import task

source_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")

@task
def qtgen(c):
    """
    Generate all py files from ui files
    """
    component_dir = os.path.join(source_dir, "gui", "components")

    for filename in os.listdir(component_dir):
        if filename.endswith(".ui"):
            full_path = os.path.join(component_dir, filename)
            c.run(f"pyuic5 {full_path} -o {full_path.replace('.ui', '.py')}")
@task
def start(c):
    """
    Start the program
    """
    main_path = os.path.join(source_dir, "main.py")
    c.run(f"python {main_path}")

