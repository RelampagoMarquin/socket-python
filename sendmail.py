import smtplib
import ssl
import email.message

setor = 'B'
nome = 'Equipe do Financeiro'
msg = email.message.Message()
msg['Subject'] = f"Planilha Financeiro para departamento: {setor}"


body = f"""
<p>Olá, {nome}</p>
<p>Segue em anexo a planilha com os resultados desse mês</p>
<p>Atenciosamente,</p>
<p>Gerente ADM</p>
"""

msg['From'] = 'SEUMAIL@gmail.com'
msg['To'] = 'SEUMAIL@gmail.com'
password = 'SUASENHA'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls (context=context)
    conexao.login(msg['From'], password)
    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))