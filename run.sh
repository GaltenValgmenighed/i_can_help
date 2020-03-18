#!/bin/bash
docker run -d --name gavakut \
--rm \
-v $PWD/helper:/app/helper \
-v $PWD/helpee:/app/helpee \
-e "LETSENCRYPT_HOST=nextcloud.khebbie.dk" \
-e "LETSENCRYPT_EMAIL=khebbie@protonmail.com" \
-e "VIRTUAL_HOST=nextcloud.khebbie.dk" \
gavakut
