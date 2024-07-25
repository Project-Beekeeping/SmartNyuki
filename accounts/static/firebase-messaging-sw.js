importScripts('https://www.gstatic.com/firebasejs/9.6.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.1/firebase-messaging-compat.js');

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyC3ANmOdzhjPgxWq91vx_qnpVMpDq-qhig",
    authDomain: "projectmain1-44cce.firebaseapp.com",
    databaseURL: "https://projectmain1-44cce-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "projectmain1-44cce",
    storageBucket: "projectmain1-44cce.appspot.com",
    messagingSenderId: "592837634615",
    appId: "1:592837634615:web:ca63818dd7101534dc6db2",
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

// Handle incoming push messages
self.addEventListener('push', (event) => {
  console.log('[firebase-messaging-sw.js] Push event received:', event);

  const data = event.data ? event.data.json() : {};
  const title = data.notification ? data.notification.title : 'Default Title';
  const options = {
    body: data.notification ? data.notification.body : 'Default body text',
    icon: data.notification ? data.notification.icon : '/firebase-logo.png',
    data: data.notification ? data.notification : {},
  };

   // Check if messageId is available
  if (data.messageId) {
    console.log('Message ID:', data.messageId);
  } else {
    console.log('No Message ID received.');
  }

  event.waitUntil(
    self.registration.showNotification(title, options)
      .catch(error => {
        console.error('[firebase-messaging-sw.js] Error showing notification:', error);
      })
  );
});

// Handle background messages
messaging.onBackgroundMessage((payload) => {
  console.log('[firebase-messaging-sw.js] Received background message:', payload);

  const notificationTitle = payload.notification ? payload.notification.title : 'Default Title';
  const notificationOptions = {
    body: payload.notification ? payload.notification.body : 'Default body text',
    icon: payload.notification ? payload.notification.icon : '/firebase-logo.png',
  };

  self.registration.showNotification(notificationTitle, notificationOptions)
    .catch(error => {
      console.error('[firebase-messaging-sw.js] Error showing background notification:', error);
    });
});
