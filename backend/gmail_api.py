import base64
import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# If modifying these scopes, delete the token.json file if it exists.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def create_message(sender, to, subject, message_text):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message.attach(MIMEText(message_text, 'plain'))
    print('Message created')
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')}

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        print('Message sent successfully!')
        return message
    except HttpError as error:
        print('An error occurred: %s' % error)
        print(error.content)

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Use the authenticated service to send an email
    sender_email = "nectariawebstore@gmail.com"  # Replace with the sender's email address
    recipient_email = "nectariawebstore@gmail.com"  # Replace with the recipient's email address
    subject = "Test Email"
    message_text = "This is a test email sent from the Gmail API using OAuth 2.0 Client IDs."
    print('Email created')

    message = create_message(sender_email, recipient_email, subject, message_text)
    send_message(service, user_id='me', message=message)

if __name__ == '__main__':
    main()

#sender_email = "nectaria@nectaria-webstore.iam.gserviceaccount.com"
#recipient_email = "nectariawebstore@gmail.com"