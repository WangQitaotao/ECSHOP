# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/8 15:32
@作者 ： 王齐涛
@文件名称： send_email.py
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.read_yaml import ReadYaml
from loggingtest.logger_handler_v3 import GetLogger


def send_Email_qq(file_path):
    # 读取yaml文件中的参数
    re = ReadYaml().read_yaml("./config/email_data")
    mail_name = re["email_qq"]["name"]
    mail_host = re["email_qq"]["host"]  # 腾讯企业邮箱服务器地址   #qq:smtp.qq.com
    mail_user = re["email_qq"]["user"]
    mail_pass = re["email_qq"]["pass"]  # 授权码
    receivers = [re["email_qq"]["recipients"]]   # 收件人邮箱，注意用[]，可以群发

    # 设置email信息
    message = MIMEMultipart()
    message["From"] = mail_user  # 头部信息
    message["Subject"] = re["email_qq"]["subject"]    # 标题

    # 设置群发
    if len(receivers)>1:
        message["To"] = ",".join(receivers)     # 以“，”为分隔符，将联系人分隔
    else:
        message["To"] = receivers[0]

    # 设置邮箱的正文信息
    part1 = MIMEText(re["email_qq"]["part"], "plain", "utf-8")

    # 添加一个文本附件
    part2 = MIMEText(open(f"{file_path}","r").read(),"plain","utf-8")
    part2["Contype-Type"] = 'application/octet-stream'   # 设置附件的内容类型，一般设置为二进制流
    part2["Content-Disposition"] = 'attachment; filename="index.html"' # 设置附件头，添加文件名
    message.attach(part1)
    message.attach(part2)

    # 登录发送
    try:
        server = smtplib.SMTP_SSL(mail_host,465)    # 还可以写成server = smtplib.SMTP_SSL()   server.connect(mail_host,465)
        server.login(mail_user,mail_pass)   # 登录
        server.sendmail(mail_user,receivers,message.as_string())   # 发送邮件
        server.quit()
        GetLogger().debug(f"{mail_name}邮箱发送成功 --> 收件人:{receivers}")
    except Exception as e:
        GetLogger().info(f"{mail_name}邮箱发送失败 --> 报错提示:{e}")


