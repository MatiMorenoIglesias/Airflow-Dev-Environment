kubectl create secret docker-registry $DOCKER_SECRET_NAME -n $NAMESPACE \
  --docker-server=$DOCKER_SERVER \
  --docker-username=$DOCKER_USERNAME \
  --docker-password=$DOCKER_PASSWORD \
  --docker-email=$DOCKER_EMAIL
