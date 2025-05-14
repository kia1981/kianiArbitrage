import requests

TOKEN = '7655818605:AAETqUPpBhOAKZ-vmgPf4e8B5ILfcZSQnd8'
WEBHOOK_URL = 'https://kia1981.pythonanywhere.com/webhook'

# تنظیم Webhook
url = f'https://api.telegram.org/bot{7655818605:AAETqUPpBhOAKZ-vmgPf4e8B5ILfcZSQnd8}/setWebhook'
response = requests.post(url, data={'url': WEBHOOK_URL})

if response.status_code == 200:
    print("Webhook successfully set!")
else:
    print("Failed to set webhook:", response.status_code)
