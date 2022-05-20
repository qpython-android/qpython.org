#!/bin/bash
rm -fr ../docs
make html

#mv static static
#mv sources sources

cd build/html && find . -name "*.html" -exec python2 ../../add-analytics.py {} \; && find . -name "*.html" -exec sed -i -e 's/_static/static/g;s/_images/images/g' {} \; && find . -name "*-e" -exec rm {} \; && mv _static static && mv _images  images

cd ../.. && mv build/html  ../docs && cp CNAME ../docs  && cp -r quick-start ../docs && cp favicon.ico  ../docs && cp index.html ../docs && cp community.html discord.html privacy.html privacy-cn.html agreement-cn.html agreement.html qlua-privacy.html qlua-rate.html qpy3-rate.html ../docs && cp -r market ../docs
