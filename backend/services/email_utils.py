import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI

# ✅ Directly define credentials here (since you are not using .env)
OPENAI_API_KEY = "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"
EMAIL_USER = "yourcompanyemail@gmail.com"
EMAIL_PASS = "lucz tkzg bzxs mkvk"  # Gmail app password
EMAIL_RECEIVER = EMAIL_USER  # default recipient (company inbox)

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def send_email(to_email, subject, body):
    """Send email through Gmail SMTP."""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print(f"✅ Email sent to {to_email}")
        return True
    except Exception as e:
        print(f"❌ Email send error: {e}")
        return False


def generate_auto_reply(name, message, to_email=None):
    """Generate an AI-powered auto-reply and optionally email it to the user."""
    try:
        # Step 1 — Use OpenAI to generate a professional reply
        prompt = f"Write a short, polite email reply as Mastersolis Infotech to {name}, who said: '{message}'."
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        reply_text = completion.choices[0].message.content.strip()

        # Step 2 — Send auto-reply email to user if email is provided
        if to_email:
            subject = f"Thank you for contacting Mastersolis Infotech, {name}!"
            send_email(to_email, subject, reply_text)

        # Step 3 — Also send notification to company inbox
        company_subject = f"New Contact Message from {name}"
        company_body = f"Name: {name}\nEmail: {to_email}\nMessage: {message}\n\nAI Reply:\n{reply_text}"
        send_email(EMAIL_RECEIVER, company_subject, company_body)

        return reply_text

    except Exception as e:
        print(f"❌ AI auto-reply error: {e}")
        return f"Hi {name}, thank you for reaching out! We’ll get back to you soon."