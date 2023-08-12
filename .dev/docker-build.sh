#/bin/bash
# SQLITE_BUILD=True
REPO_NAME="${PWD##*/}"
REPO_NAME_LOWER="$(echo "$REPO_NAME" | tr '[:upper:]' '[:lower:]')"
if [ "$SQLITE_BUILD" = "True" ]; then
  echo "SQLITE_BUILD=$SQLITE_BUILD Build with sqlite database"
else
  echo "SQLITE_BUILD=$SQLITE_BUILD Build with manage.bin"
fi
docker build . -t $REPO_NAME_LOWER
docker run --rm -v $PWD/dist:/$REPO_NAME/dist -e SQLITE_BUILD=$SQLITE_BUILD --name $REPO_NAME_LOWER-build $REPO_NAME_LOWER