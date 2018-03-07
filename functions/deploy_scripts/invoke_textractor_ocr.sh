aws lambda invoke \
--invocation-type Event \
--function-name DEV-textractor-ocr \
--region us-east-1 \
--payload file://lambda_input.txt \
--profile adminuser \
outputfile.txt
