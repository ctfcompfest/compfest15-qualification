pushd frontend
    mv .env .env.orig
    cat > .env << EOF
VITE_WS_URL=ws://localhost:555
VITE_PRIME_URL=http://localhost:555/prime
EOF
    yarn install
    yarn build
    mv .env.orig .env
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
