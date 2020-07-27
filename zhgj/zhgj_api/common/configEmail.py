#__author__'daolin yang'
# coding:utf-8
#/usr/bin/python

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
#from email.mime.image import MIMEImage
from datetime import datetime
import threading
import config as config
from common.Log import MyLog
import zipfile
import glob
#from bs4 import BeautifulSoup
#import html5lib


localReadConfig = config.config()


class Email:
    def __init__(self):
        global host, user, password, port, sender, title,receiver
        host = localReadConfig.get_email("mail_server")
        user = localReadConfig.get_email("mail_username")
        password = localReadConfig.get_email("mail_password")
#        port = localReadConfig.get_mail("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")
#        receiver=localReadConfig.get_email("receiver")
        content = localReadConfig.get_email("content")

        # get receiver list
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        for n in str(self.value).split(","):
            self.receiver.append(n)

        # defined email subject
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "Interface test Report" + " " + date

        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('related')

    def config_header(self):
        """
        defined email header include subject, sender and receiver
        :return:
        """
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        #define report content
        reportpath = open(os.path.join(self.log.get_result_path(),"report.html"),encoding='utf-8')
        mail_body=reportpath.read()
        reportpath.close()

        #RESLOVED OUTLOOK can not use javascript
        """
        soup=BeautifulSoup(mail_body,'html5lib')
        soup.find('p', id='show_detail_line').decompose()
        links = soup.find_all('a')
        for n in links:
            n.decompose()
        """
        #define email template
        f = open(os.path.join(config.fileDir, 'TestFile', 'email.html'))
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)
 #       self.config_image()

    """
    def config_image(self):
        # defined image path
        image1_path = os.path.join(config.proDir, 'testFile', 'img', 'logo.png')
        fp1 = open(image1_path, 'rb')
        msgImage1 = MIMEImage(fp1.read())
        # self.msg.attach(msgImage1)
        fp1.close()

        # defined image id
        msgImage1.add_header('Content-ID', '<image1>')
        self.msg.attach(msgImage1)
    """
    def config_file(self):

        if self.check_file():

            reportpath = self.log.get_result_path()
            zippath = os.path.join(config.fileDir, "result", "Interface test report.zip")

            # zip file
            files = glob.glob(reportpath + '\*')
            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            for file in files:
                # 修改压缩文件的目录结构
                f.write(file, '/report/'+os.path.basename(file))
            f.close()

            reportfile = open(zippath, 'rb').read()
            filehtml = MIMEApplication(reportfile)
            filehtml.add_header('Content-Disposition','attachment',filename="Interface test report.zip")
            #solve attach issue for dreawer system compatibility
            #filehtml = MIMEText(reportfile, 'base64', 'utf-8')
            #filehtml['Content-Type'] = ('application/octet-stream','name="Interface test report.zip"')
            #filehtml['Content-Disposition'] = 'attachment; filename="Interface test report.zip"'
            self.msg.attach(filehtml)

    def check_file(self):
        reportpath = self.log.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            self.logger.error(str(ex))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()
