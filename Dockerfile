FROM uccser/django:2.2.12

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive
ENV DJANGO_PRODUCTION=True

RUN apt-get update \
    && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    --no-install-recommends --no-install-suggests \
    && apt-get -y --purge autoremove \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8080
RUN mkdir /dthm4kaiako
WORKDIR /dthm4kaiako

# Copy and install Python dependencies
COPY requirements /requirements
RUN /docker_venv/bin/pip3 install -r /requirements/production.txt

ADD ./dthm4kaiako /dthm4kaiako/

CMD /dthm4kaiako/docker-production-entrypoint.sh
