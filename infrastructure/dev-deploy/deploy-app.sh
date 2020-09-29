#!/bin/bash

source ./infrastructure/dev-deploy/load-dev-deploy-config-envs.sh

# Deploys the application to Google App Engine

# Install Google Cloud SDK
./infrastructure/install_google_cloud_sdk.sh

# Decrypt secret files archive that contain credentials.
./infrastructure/dev-deploy/decrypt-dev-secrets.sh

# Load environment variables.
source ./dthm4kaiako/load-dev-envs.sh

# Authenticate with gcloud tool using the decrypted service account credentials.
# See: https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account
gcloud auth activate-service-account --key-file ./dthm4kaiako/${GOOGLE_APPLICATION_CREDENTIALS}

# Create empty SSH keys with an empty passphrase, for Google Cloud SDK to
# copy files to a VM for building the Docker image.
# Only required for deploying to Google App Engine flexible environment.
# See: https://cloud.google.com/solutions/continuous-delivery-with-travis-ci#continuous_deployment_on_app_engine_flexible_environment_instances
ssh-keygen -q -N "" -f ~/.ssh/google_compute_engine

# Create app.yaml file using environment variables.
python ./infrastructure/replace_envs.py ./infrastructure/dev-deploy/app.yaml

# Start system
./dev start
./dev update

# Publish Django system to Google App Engine.
#
# This deploys using the 'app.yaml' completed earlier that contains
# secret environment variables to use within the application.
# Project is specified to ensure correct project deployment.
# Runs with '--quiet' to skip prompt of confirmation.
# If multiple services are deployed at a later stage, these should be checked
# that the apps deploy to the correct services.
# See: https://cloud.google.com/sdk/gcloud/reference/app/deploy
gcloud app deploy ./app.yaml --quiet --project=dthm4kaiako-dev

# Publish cron jobs to Google App Engine.
cp ./infrastructure/dev-deploy/cron.yaml ./cron.yaml
gcloud app deploy ./cron.yaml --quiet --project=dthm4kaiako-dev --promote --stop-previous-version
