import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Relatório Diário - Invocado pelo Python'
msg['From'] = 'contatestedev777@gmail.com'
msg['To'] = 'caiocesar.dev.ti@gmail.com'
msg.set_content('Segue o relatório gerado automaticamente.')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('contatestedev777@gmail.com', 'qmux tryt lpza fyli')
    smtp.send_message(msg)

print("E-mail enviado automaticamente!")
