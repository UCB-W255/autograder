az acr login --name w255mids
az aks get-credentials --name w255-aks --resource-group w255 --overwrite-existing --admin

IMAGE_NAME=w255midssensitive.azurecr.io/winegarj/autograder
LABEL=$(git rev-parse --short HEAD)
TAG=${IMAGE_NAME}:${LABEL}

docker build --platform linux/amd64 -t ${TAG} .
docker push ${TAG}

sed -i '' "s/w255midssensitive.azurecr.io\/.*/w255midssensitive.azurecr.io\/winegarj\/datacollector:${LABEL}/" infra/deployment.yaml
kubectl apply -f infra/namespace.yaml
kubectl apply -f infra/
