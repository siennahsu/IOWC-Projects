#!/bin/bash

cd /Users/Sienna/Sites/IOWC_site/scripts
chmod +x scripts/set_env_vars.sh
source scripts/set_env_vars.sh
cd /Users/Sienna/Sites/IOWC_site/historical-climate-data-main/api
npm install
npm run start:dev