import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Datos del correo
remitente = "" # Coloca aquí el remitente del correo
destinatario = "" # Coloca aquí el destinataio del correo
password = ""  # Coloca aquí tu contraseña de aplicación

# Crear mensaje multipart
mensaje = MIMEMultipart()
mensaje['Subject'] = "📊 Resultados de Medición de Distancia"
mensaje['From'] = remitente
mensaje['To'] = destinatario

# Cuerpo de texto
cuerpo = """
Se han calculado los resultados de la medición de distancia entre dos puntos.

Adjunto se encuentra:
1. La imagen con los puntos marcados.
2. El archivo de texto con los detalles de la distancia.

Gracias.
"""
mensaje.attach(MIMEText(cuerpo, "plain"))

# Adjuntar imagen resaltada
with open("resultado_con_puntos.jpg", "rb") as img:
    imagen_adjunto = MIMEImage(img.read())
    imagen_adjunto.add_header('Content-Disposition', 'attachment', filename="resultado_con_puntos.jpg")
    mensaje.attach(imagen_adjunto)

# Adjuntar archivo de texto con los resultados
with open("resultados.txt", "rb") as txt_file:
    parte_txt = MIMEBase("application", "octet-stream")
    parte_txt.set_payload(txt_file.read())
    encoders.encode_base64(parte_txt)
    parte_txt.add_header(
        "Content-Disposition",
        f"attachment; filename=resultados.txt"
    )
    mensaje.attach(parte_txt)

# Enviar correo
try:
    servidor = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    servidor.login(remitente, password)
    servidor.send_message(mensaje)
    servidor.quit()
    print("[✅] Correo enviado con imagen y archivo de texto adjuntos.")
except Exception as e:
    print(f"[❌] Error al enviar correo: {e}")
