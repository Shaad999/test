import requests
import json

# ফোন নাম্বার গ্রহণ
phone = input("Enter number:>> ")  # এখানে আপনার ফোন নাম্বার দিন

# API URL
url = "https://api.betonbook.com/api/v5/auth/otp/request"

# POST ডাটার জন্য পে-লোড প্রস্তুত
payload = {
    "phone": phone,
    "language": 1
}

# HTTP Headers
headers = {
    "Content-Type": "application/json",
}

# POST Request পাঠানো
try:
    # `json=payload` ব্যবহার করলে `json.dumps` প্রয়োজন হয় না
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # HTTP এরর থাকলে ব্যতিক্রম ছুঁড়ে দেবে
    print(response.text)  # সার্ভারের উত্তর প্রিন্ট করা
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
