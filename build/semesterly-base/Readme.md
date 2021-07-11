This builds the base image we use. To update:

docker build -t horariotec-base .
docker tag horariotec-base:latest sgerli/horariotec-base:latest
docker push sgerli/horariotec-base:latest

Or multiplatform builds with buildx:
docker buildx build --platform linux/arm64,linux/amd64 . -t sgerli/horariotec-base -t sgerli/horariotec-base:latest -t sgerli/horariotec-base:latest --push
