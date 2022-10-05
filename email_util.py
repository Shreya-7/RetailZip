import smtplib
import ssl
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import xlwt
from xlwt import Workbook


def get_subject(request_number):
    return 'Your Consultation Request at RetailZip (' + request_number + ')'


def get_text_content(data, request_number):

    content = '''/
        Dear {client_name},
        \n]\n
        Thank you for showing interest in RetailZip Solutions. \n\n
        Your consultation request number is {request_number}. Please refer to this number for all future correspondences.\n\n
        We are studying your consultation request and will get back to you at the earliest.\n\n
        Please find below the details of your consultation request as submitted by you:\n\n
    '''.format(client_name=data['name'], request_number=request_number)

    for key, value in data.items():
        info = '{key}: {value}\n\n'.format(key=key, value=value)
        content += info

    footer = '''/
        Namaste\n\n
        Manish\n\n
        Founder, RetailZip\n\n
        +91 9339725675\n\n
        manish@retailzip.in\n\n
        https://www.retailzip.in\n\n
    '''
    return content + footer


def get_html_content(data, request_number):

    html = '''\
            <html>
                <head>
                </head>
                <body>
                    <p>Dear {client_name}, </p>
                    <br>
                    <p>
                        Thank you for showing interest in
                        <b>
                            <span style='color: #ee4631'>Retail</span><span style='color: #0f60b2'>Zip</span>
                            Solutions. 
                        </b>
                    </p>
                    <p>
                        <b>Your consultation request number is
                        <span style='color: #0f60b2'>{request_number}</span>.
                        </b>
                        Please refer to this number for all future correspondences.
                    </p>

                    <p>
                        Please find below the details of your consultation request as submitted by you:
                    </p>
                    <br>
                </body>
            </html>
            '''.format(client_name=data['name'], request_number=request_number)

    for key, value in data.items():

        if value != '':
            info = '<b>{key}</b>: {value}<br>'.format(
                key=key.title(), value=value)
            html += info

    html += '<p>We are studying your consultation request and will get back to you at the earliest.</p>'

    footer = '''\
        <b>
            Namaste <br>
            Manish <br>
            Founder, 
                <span style='color: #ee4631'>Retail</span><span style='color: #0f60b2'>Zip</span>
            
        </b><br>
        +91 9339725675 <br>
        <a href='mailto:manish@retailzip.in'>manish@retailzip.in</a> <br>
        <a href='https://www.retailzip.in'>https://www.retailzip.in</a>
    '''
    return html + '<br>' + footer


def create_excel_sheet(data, request_number):
    """
        Create an excel sheet containing request details to be attached to the reference email.
    """
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    sheet1.write(0, 0, 'Ref. No.')
    sheet1.write(1, 0, request_number)

    start = 1
    for key, value in data.items():
        sheet1.write(0, start, key.title())
        sheet1.write(1, start, value)

        start += 1

    wb.save('submission.xls')


def send_email(data, request_number):

    # create_excel_sheet(data, request_number)

    sender_email, password = 'manish@retailzip.in', os.getenv('RZ_EMAIL_PASS')
    port = 465
    smtp_server = 'smtpout.secureserver.net'

    receiver_email = data['email']

    message = MIMEMultipart('alternative')
    message['Subject'] = get_subject(request_number)
    message['From'] = sender_email
    message['To'] = receiver_email

    text_obj = MIMEText(get_text_content(data, request_number), 'plain')
    html_obj = MIMEText(get_html_content(data, request_number), 'html')

    message.attach(text_obj)
    message.attach(html_obj)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)

        # send email to the client
        server.sendmail(sender_email, receiver_email, message.as_string())

        # prepare the reference email
        # filename = 'submission.xls'

        # with open(filename, 'rb') as attachment:
        #     part = MIMEBase('application', 'octet-stream')
        #     part.set_payload(attachment.read())

        # encoders.encode_base64(part)

        # part.add_header(
        #     'Content-Disposition',
        #     f'attachment; filename= {filename}',
        # )
        # message.attach(part)
        server.sendmail(
            sender_email, 'retailzip21@gmail.com', message.as_string())

    # os.remove('submission.xls')
