from typing import Any
def generate_files(template_directory: str, output_dir: str, context: dict[str, Any]):
    from cookiecutter import generate
    generate.generate_files(
        context={
            "cookiecutter": context,
        },
        repo_dir=template_directory,
        overwrite_if_exists=True,
        output_dir=dags_dir
    )
if __name__ == "__main__":
    print("Generate File process started")
    import sys, os, json
    from typing import Any
    dags_dir = sys.argv[1]
    templates_dir = sys.argv[2]
    workflows_dir = sys.argv[3]
    for wf_dir in os.listdir(f"{workflows_dir}"):
        workflow_file = f"{workflows_dir}/{wf_dir}/cookiecutter.json"
        if os.path.exists(workflow_file):
            with open(workflow_file,"r") as file:
                context = json.load(file)
                template_name = context["process"]["template"]
                process_values = context["process"]["values"]
                template_dir = f"{templates_dir}/{template_name}/src"
                if os.path.exists(template_dir):
                    try:
                        generate_files( output_dir= dags_dir ,context=process_values, template_directory=template_dir)
                    except Exception as e:
                        print(str(e))
                else:
                    print("template doesn't exists")
        else:
            print(f"{workflow_file} does not exists.")
