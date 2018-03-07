aws lambda create-function \
--region "us-east-1" \
--function-name "DEV-textractor-ocr" \
--zip-file "fileb://../ocr/main.zip" \
--role "arn:aws:iam::457807691790:role/service-role/Lambda_role" \
--handler main.handle \
--runtime python3.6 \
--profile adminuser \
--timeout 10 \
--memory-size 1024
