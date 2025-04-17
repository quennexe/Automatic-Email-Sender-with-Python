
from email_sender import send_email

def main():
    print("📧 Otomatik E-posta Gönderici")
    print("Birden fazla alıcı için e-posta adreslerini virgül (,) ile ayırın.")

    to_input = input("Alıcı e-posta adresleri: ")  
    subject = input("Konu: ")
    body = input("Mesaj içeriği: ")

 
    to_list = [email.strip() for email in to_input.split(",")]

    send_email(to_list, subject, body)

if __name__ == "__main__":
    main()
