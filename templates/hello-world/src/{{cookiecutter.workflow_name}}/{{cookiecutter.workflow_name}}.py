from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
NAMESPACE="{{cookiecutter.namespace}}"
IMAGE_NAME="registry.digitalocean.com/mmoreno-dev-registry-sandbox/helloworld-jobtemplate"
IMAGE_VERSION="v0.1.0"
executor_config = {
    "KubernetesExecutor": {
        "resources": {
            "requests": {
                "memory": "256Mi",
                "cpu": "500m"
            },
            "limits": {
                "memory": "512Mi",
                "cpu": "1000m"
            }
        }
    }
}

compute_resources = {
    'request_memory': '256Mi',
    'request_cpu': '500m',
    'limit_memory': '512Mi',
    'limit_cpu': '1000m'
}

default_dag_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now()
}


with DAG(
    dag_id="{{cookiecutter.workflow_name}}-job",
    start_date=datetime.now(),
    default_args=default_dag_args,
    schedule="0 0 */1 * * *",
) as dag:
    k8s_operator = KubernetesPodOperator(
        namespace='airflow',
        image=f"registry.digitalocean.com/mmoreno-dev-registry-sandbox/helloworld-jobtemplate:v0.1.0",
        cmds=["python3", "hello-world.py"],
        task_id="hello-world",
        name="hello-world",
        container_resources=compute_resources,
        image_pull_policy="Always",
        image_pull_secrets="my-docker-secret"
    )

    """
    KubernetesPodOperator(
        namespace=NAMESPACE,
        image=f"{IMAGE_NAME}:{IMAGE_VERSION}",
        name="k8s_op",
        compute_resources=compute_resources,
        is_delete_operator_pod=False,
        cmds=["python3", "Matias"],
        arguments=[""],
        get_logs=True,
        task_id="dry_run_demo",
        resources={
            'request_memory': '256Mi',
            'request_cpu': '500m',
            'limit_memory': '512Mi',
            'limit_cpu': '1000m'
        }
    )
    """
    k8s_operator.dry_run()
