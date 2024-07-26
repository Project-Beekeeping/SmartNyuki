from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
import firebase_admin
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from firebase_admin import messaging
from datetime import datetime
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Threshold
from .utils import send_push_notification, absAppPath
import json, base64
from .firebase_config import messaging
from django.urls import reverse
from django.views.generic import View
from firebase_admin import firestore # type: ignore
''' from pyfcm import FCMNotification # type: ignore '''
from django.conf import settings as st
import requests
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.contrib.auth import logout
from .models import Hive, FCMToken
from .forms import LoginForm

ACC_TOKEN = ""

@csrf_exempt
@login_required
def save_token(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        if token:
            profile = request.user.profile
            profile.fcm_token = token
            profile.save()
            return JsonResponse({'message': 'Token saved successfully'})
        return JsonResponse({'error': 'No token provided'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def send_notification_to_all(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notifications',
        {
            'type': 'send_notification',
            'message': message
        }
    )

def send_notification_view(request):
    channel_layer = get_channel_layer()
    message = {"message": "Test notification from Django view"}
    async_to_sync(channel_layer.group_send)(
        "notifications",  # Replace with your group name
        {
            "type": "send_notification",
            "message": message
        }
    )
    return JsonResponse({"status": "Notification sent"})

@login_required
def sensor_data_view(request, hive_id):
    db = firestore.client()
    hive_ref = db.collection('hives').document(hive_id)
    hive_data = hive_ref.get().to_dict()
    
    hive = Hive.objects.get(id=hive_id)
    temperature = hive_data.get('temperature')
    humidity = hive_data.get('humidity')
    sound_level = hive_data.get('sound_level')

    notifications = []
    if temperature is not None:
        if temperature < hive.temperature_threshold_low:
            notifications.append(f"Temperature threshold exceeded: {temperature}°C")
        if temperature > hive.temperature_threshold_high:
            notifications.append(f"Temperature threshold exceeded: {temperature}°C")
    
    if humidity is not None:
        if humidity < hive.humidity_threshold_low:
            notifications.append(f"Humidity threshold exceeded: {humidity}%")
        if humidity > hive.humidity_threshold_high:
            notifications.append(f"Humidity threshold exceeded: {humidity}%")
    
    if sound_level is not None:
        if sound_level > hive.sound_threshold_high:
            notifications.append(f"Sound level threshold exceeded: {sound_level} dB")

    context = {
        'hive_id': hive_id,
        'temperature': temperature,
        'humidity': humidity,
        'sound_level': sound_level,
        'notifications': notifications,
    }
    return render(request, 'profile.html', context)

db = firestore.client()

def send_notification(registration_ids, message_title, message_desc):
    fcm_api = "55ad0de6a76ed5efac019b6ba7b2ad671502872e"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
        "Content-type" : "application/json",
        "Authorization": 'key='+fcm_api
    }
    
    payload = {
        "registration_ids" : registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
        }
        
    }
    result = requests.post(url, data=json.dumps(payload), headers=headers)
    print(result)

def send_test_notification(request):
    registration = ACC_TOKEN
    send_notification(registration, 'Hive Condition', 'Temperature for Hive1 is too high')
    return HttpResponse({"msg": "sent"})

    
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! - You are successflly SignUped!")
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
        return redirect('signin')
    else:
        form = LoginForm()
    return render(request, 'signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, Email=Email, password=password)
            if user:
                login(request, user)    
                return redirect('dashboard')
        return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('reset-email')

        message = 'Password reset email sent!'
        return render(request, 'password.html_reset', {'message': message})

    return render(request, 'password_reset.html')


def hives(request):
    return render(request, 'hives.html')

def subscription(request):
    return render(request, 'subscription.html')

def profile(request):
    return render(request, 'profile.html')

def profile1(request):
    return render(request, "profile1.html")


def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout')
    return render(request, 'signin.html')

def settings(request):
    return render(request, 'settings.html')


@login_required
def sensor_data_view(request, hive_id):
    # Retrieve sensor data and check thresholds for a specific hive
    user_token = request.user.profile.fcm_token
    thresholds = Threshold.objects.filter(hive_id=hive_id)

    for threshold in thresholds:
        if sensor_data.exceeds_threshold(threshold):
            message = f"Threshold exceeded for {threshold.parameter}: {sensor_data.value}"
            send_push_notification(user_token, 'Threshold Exceeded', message)

    return render(request, 'sensor_data.html', context)

@login_required
@csrf_exempt  
def initiate_payment(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')  # Assuming 'mpesa' for M-Pesa payment method
        
        # Replace with your actual M-Pesa API endpoint and credentials
        api_endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'

        # Replace with your logic to fetch user's phone number
        user_phone_number = request.user.profile.phone  # Replace with how you retrieve user's phone number

        # Fetch OAuth token
        def get_oauth_token(consumer_key, consumer_secret):
            oauth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
            response = requests.get(oauth_url, auth=(consumer_key, consumer_secret))
            if response.status_code == 200:
                return response.json().get('access_token')
            return None

        access_token = get_oauth_token(consumer_key, consumer_secret)
        if not access_token:
            return JsonResponse({'success': False, 'error': 'Failed to retrieve access token'})

        # Generate timestamp and password
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode((business_shortcode + lipa_na_mpesa_online_passkey + timestamp).encode('utf-8')).decode('utf-8')

        # Construct your request to M-Pesa API
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        payload = {
            'BusinessShortCode': business_shortcode,
            'Password': password,
            'Timestamp': timestamp,
            'TransactionType': 'CustomerPayBillOnline',
            'Amount': '1000',  # Replace with actual subscription amount
            'PartyA': user_phone_number,
            'PartyB': business_shortcode,  # Typically your paybill or till number
            'PhoneNumber': user_phone_number,
            'CallBackURL': 'YOUR_CALLBACK_URL',
            'AccountReference': 'YOUR_ACCOUNT_REFERENCE',
            'TransactionDesc': 'Subscription Payment',
        }

        try:
            response = requests.post(api_endpoint, headers=headers, json=payload)
            response_data = response.json()
            if response.status_code == 200 and response_data.get('ResponseCode') == '0':
                return JsonResponse({'success': True, 'message': 'Payment initiated. Please confirm on your phone.'})
            else:
                error_message = response_data.get('errorMessage', 'Failed to initiate payment.')
                return JsonResponse({'success': False, 'error': error_message})
        except Exception as e:
            print(f"Error initiating payment: {e}")
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def firebase_messaging_sw_js(request):
    filename = 'firebase-messaging-sw.js'
    filepath = absAppPath('accounts', 'static', filename)
    try:
        with open(filepath, 'rb') as jsfile:
            response = HttpResponse(jsfile.read(), content_type='application/javascript')
            response['Content-Disposition'] = f'inline; filename="{filename}"'
            return response
    except FileNotFoundError:
        return HttpResponse(status=404)


@csrf_exempt
def save_fcm_token(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            token = body.get('token')
            ACC_TOKEN = token
            return JsonResponse({'message': 'Token saved successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)