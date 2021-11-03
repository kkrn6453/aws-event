import requests
import json
import os

# definition env of DingDing
dd_flag = os.getenv('dd_flag')
dd_sk = os.getenv('dd_sk')

def send_msg_dd(msg):
    url_dd = "https://oapi.dingtalk.com/robot/send?access_token="
    url_dd = url_dd + dd_sk
    headers = {'Content-Type': 'application/json'}
    values = """{
      "msgtype":"text",
      "text":{
        "content": "%s"
      }
      }""" % msg
    requests.post(url_dd, values.encode("utf-8"), headers=headers)

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    Message = json.loads(event['Records'][0]['Sns']['Message'])

    #Message = json.loads(event)
    print('Message received from SNS:', Message)
    msg_type = Message['detail-type']#.replace(" ", "")
    msg_id = Message['id']
    msg_account = Message['account']
    msg_time = Message['time']
    msg_region = Message['region']

    if msg_type == "AWS Health Event":  # 06
        print("MSG type: AWS Health Event")
        #msg_severity = Message['detail']['severity']
        msg_service = Message['detail']['service']
        #msg_desc = Message['detail']['eventDescription']
        msg_start = Message['detail']['startTime']
        msg_TypeCode = Message['detail']['eventTypeCode']
        msg_TypeCategory = Message['detail']['eventTypeCategory']
        msg_Description = Message['detail']['eventDescription'][0]['latestDescription']
        msg = "【AWS Health Event】\n" \
              + "时间: " + msg_time + "\n\n" \
              + "【错误详细内容】\n" \
              + "账号: " + msg_account + "\n" \
              + "区域: " + msg_region + "\n" \
              + "服务: " + msg_service + "\n" \
              + "开始时间: " + msg_start + "\n" \
              + "结束时间: " + msg_start + "\n" \
              + "消息类型: " + msg_TypeCode + "\n" \
              + "事件类别: " + msg_TypeCategory + "\n\n" \
              + "【其他参考信息】\n" \
              + "消息编号: " + msg_id + "\n" \
              + "错误描述: " + msg_Description + "\n"

    if msg_type == "AWS Health Abuse Event":  # 06
        print("MSG type: AWS Health Abuse Event")
        #msg_severity = Message['detail']['severity']
        msg_service = Message['detail']['service']
        #msg_desc = Message['detail']['eventDescription']
        msg_start = Message['detail']['startTime']
        msg_TypeCode = Message['detail']['eventTypeCode']
        msg_TypeCategory = Message['detail']['eventTypeCategory']
        msg_Description = Message['detail']['eventDescription'][0]['latestDescription']
        msg = "【AWS Health Event】\n" \
              + "时间: " + msg_time + "\n\n" \
              + "【错误详细内容】\n" \
              + "账号: " + msg_account + "\n" \
              + "区域: " + msg_region + "\n" \
              + "服务: " + msg_service + "\n" \
              + "开始时间: " + msg_start + "\n" \
              + "结束时间: " + msg_start + "\n" \
              + "消息类型: " + msg_TypeCode + "\n" \
              + "事件类别: " + msg_TypeCategory + "\n\n" \
              + "【其他参考信息】\n" \
              + "消息编号: " + msg_id + "\n" \
              + "错误描述: " + msg_Description + "\n"

    dd_flag = "Y"
    if dd_flag == "Y":
        print("Send health status change to Dingding.")
        send_msg_dd(msg)
        #print(json.loads(msg))
