import aws_handler
import simple_logger
logger = simple_logger.logger()
logger.info('runnint test.py')


# key = "dev-client-ben/library/draft/040117_Gemtone_Radiant_Nude_OPP_2_page.pdf"
# key = "dev-client-ben/library/draft/sub_folder/2016_BASF_CC_LysSun_TPP.pdf"
# key = "dev-client-ben/library/draft/AAssembled.pdf"
key= "dev-client-ben/library/draft/_name_has_space+plus%2Bhiphen%27.pdf"
key= "dev-client-ben/library/published/_name_has_space+plus%2Bhiphen%27.pdf"

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


sns_event = {
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-1:457807691790:dev-pdf-update:351e935b-5013-4129-b6cb-29013d2bb068",
            "Sns": {
                "Type": "Notification",
                "MessageId": "2428029d-a5d6-523b-81f0-5187b5151b61",
                "TopicArn": "arn:aws:sns:us-east-1:457807691790:dev-pdf-update",
                "Subject": "Amazon S3 Notification",
                "Message": "{\"Records\":[{\"eventVersion\":\"2.0\",\"eventSource\":\"aws:s3\",\"awsRegion\":\"us-east-1\",\"eventTime\":\"2018-03-07T16:08:34.929Z\",\"eventName\":\"ObjectCreated:Put\",\"userIdentity\":{\"principalId\":\"AWS:AIDAISHW4LNLCJT4KIH3W\"},\"requestParameters\":{\"sourceIPAddress\":\"70.29.213.203\"},\"responseElements\":{\"x-amz-request-id\":\"F58F47B513EA8109\",\"x-amz-id-2\":\"0lNGzL7p9BfzpkkwJVHpZ9zm0X8ccxlRSAwIlhCFYVjkU7iHBm5MyDcrhfJ4/H3TCzfyKBrDLK8=\"},\"s3\":{\"s3SchemaVersion\":\"1.0\",\"configurationId\":\"2a711272-168f-46bf-ad11-69786c37bdc1\",\"bucket\":{\"name\":\"dev-beehivr-bucket\",\"ownerIdentity\":{\"principalId\":\"A24ERPT90EN829\"},\"arn\":\"arn:aws:s3:::dev-beehivr-bucket\"},\"object\":{\"key\":\"" +  key + "\",\"size\":554534,\"eTag\":\"c9ca7a036361a0d47656140ac317e9e2\",\"versionId\":\"rvszlc9KvXXZzZA7T9P.L9t8KGbo7Y8x\",\"sequencer\":\"005AA00E82C26B82F7\"}}}]}",
                "Timestamp": "2018-03-07T16:08:35.076Z",
                "SignatureVersion": "1",
                "Signature": "MqdP86bJvM6isRWIwniQU9TNHOE86wh0ON7f4fxlpLRQprMJTm5h4Yv2kq6OioAJrALP1/isqbJLCqjDByig1yC1sqgHED9UwvfwYRAlad0s7v+JAqa3RP8VYoMcolU278QaUMCx/7pdJATRNuRvxBHs770sg2nv+65ppL/HO5fXmYxDJuNi34bCdhnPlEnQQOkeJQTK6Fc90XyYWNUSrqYEPQfdk4VfaDPmGdl+LWPp4lmyWN0PX6xuydsdoHC+Rydihc6329xRp/BtRlpaarcWkefK5r429VimgiubwTqPDocEVpaqVKdpfIX+KNqyb0ZTCq2vhg+ET64Sv21/yA==",
                "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem",
                "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:457807691790:dev-pdf-update:351e935b-5013-4129-b6cb-29013d2bb068",
                "MessageAttributes": {}
            }
        }
    ]
}

context = {}

aws_handler.handle(sns_event, context)
