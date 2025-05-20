#!/usr/bin/env python3
import json
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

def dynamodb_deserializer_to_json(item):
  deserializer = TypeDeserializer()
  d_item = {k: deserializer.deserialize(v) for k, v in item.items()}
  return d_item

def get_item_cust_profile(dynamo_table, cust_id):
  response = dynamo_table.get_item(Key={"CustID": cust_id})
  cust_profile = response.get("Item")
  return cust_profile

def put_item_cust_profile_table(dynamo_table, cust_profile):
  response = dynamo_table.put_item(Item=cust_profile)
  return response

def handler(event, context):
  region = os.environ['AWS_REGION']
  records = event["Records"]

  dynamodb = boto3.resource('dynamodb', region_name=region)
  dynamo_table = dynamodb.Table('CustProfile')

  for record in records:
    if record["eventName"] == "INSERT":
      
      item = dynamodb_deserializer_to_json(record["dynamodb"]["Keys"])
      cust_profile = get_item_cust_profile(dynamo_table, item["CustID"])                
      if cust_profile:
        profile = cust_profile
        profile["TotalTnValue"] = int(profile["TotalTnValue"]) + int(item["TnValue"])
      else:
        profile = dict()
        profile["CustID"] = item["CustID"]
        profile["TotalTnValue"] = item["TnValue"]

      if profile["TotalTnValue"] < 1000:
        cust_status = "Normal"
      else:
        cust_status = "Elite"

      profile["CustStatus"] = cust_status
      response = put_item_cust_profile_table(dynamo_table, profile)
        
  return {
      'statusCode': 200,
      'body': json.dumps("Success")
  }
