include .env
export
WORKFLOW_DIR=$(PWD)/workflows
deploy_airflow:
	echo "create airflow in ${NAMESPACE} using ${CHART_VERSION} chart version."
	sh bin/docker-secret.sh
	$$HELM_BIN install $$AIRFLOW_NAME \
		airflow-stable/airflow \
		--version ${CHART_VERSION} \
		--namespace ${NAMESPACE} \
		--values ./custom_values.yml

destroy_airflow:
	echo "remove $$AIRFLOW_NAME"
	$$KUBECTL_BIN -n $$NAMESPACE  delete secret/$$DOCKER_SECRET_NAME 
	$$HELM_BIN uninstall $$AIRFLOW_NAME --namespace $$NAMESPACE
web:
	$$KUBECTL_BIN port-forward svc/$$AIRFLOW_NAME-web 8080:8080 --namespace $$NAMESPACE

generate_workflows:
	python3 bin/generate_dags.py $(PWD)/dags $(PWD)/templates $(PWD)/workflows