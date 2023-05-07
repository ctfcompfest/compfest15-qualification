pushd frontend
    yarn install
    yarn build
popd

rm -rf dist/frontend
rm -rf dist/backend

mkdir -p dist/frontend
mkdir -p dist/backend

cp -r frontend/dist dist/frontend
cp backend/index.ts dist/backend
cp backend/Dockerfile dist/backend
cp backend/*.json dist/backend
cp backend/yarn.lock dist/backend
cp docker-compose.yml dist/