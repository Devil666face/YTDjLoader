#/bin/bash
SQLITE_BUILD=False
REPO_NAME="${PWD##*/}"
REPO_NAME_LOWER="$(echo "$REPO_NAME" | tr '[:upper:]' '[:lower:]')"
docker build . -t $REPO_NAME_LOWER
docker run --rm -v $PWD/dist:/$REPO_NAME/dist -e SQLITE_BUILD=$SQLITE_BUILD --name $REPO_NAME_LOWER-build $REPO_NAME_LOWER