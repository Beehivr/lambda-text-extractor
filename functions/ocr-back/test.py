import aws_handler
import simple_logger
logger = simple_logger.logger()
logger.info('runnint test.py')


# key = "dev-client-ben/library/draft/040117_Gemtone_Radiant_Nude_OPP_2_page.pdf"
key = "dev-client-ben/library/draft/AAssembled.pdf"

event = {
  "Records": [
    {
      "eventVersion": "2.0",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "s3": {
        "configurationId": "testConfigRule",
        "object": {
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901",
          "key": key,
          "size": 292000
        },
        "bucket": {
          "arn": "arn:aws:s3:::mybucket",
          "name": "dev-beehivr-bucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          }
        },
        "s3SchemaVersion": "1.0"
      },
      "responseElements": {
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH",
        "x-amz-request-id": "EXAMPLE123456789"
      },
      "awsRegion": "us-east-1",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "eventSource": "aws:s3"
    }
  ]
}

context = {}

aws_handler.handler(event, context)
