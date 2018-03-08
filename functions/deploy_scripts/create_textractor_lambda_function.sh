aws lambda create-function \
--region "us-east-1" \
--function-name "DEV-pdf-text-extractor" \
--zip-file "fileb://../simple/main.zip" \
--role "arn:aws:iam::457807691790:role/service-role/Lambda_role" \
--handler aws_handler.handle \
--runtime python3.6 \
--timeout 120 \
--memory-size 1024 \
--vpc-config "{ \"SubnetIds\": [\"subnet-45882979\", \"subnet-29fa8460\", \"subnet-891897a4\", \"subnet-69555b0c\"], \"SecurityGroupIds\": [\"sg-985117e5\"]}"
