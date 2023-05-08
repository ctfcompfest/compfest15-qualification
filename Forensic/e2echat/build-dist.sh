pushd src
  bash build.sh
  zip -r dist.zip dist
  rm -rf dist
popd

rm public/chall.zip
mv src/dist.zip public/chall.zip
