importScripts('https://www.gstatic.com/firebasejs/9.6.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.1/firebase-messaging-compat.js');
  
var firebaseConfig = {
  apiKey: "AIzaSyC3ANmOdzhjPgxWq91vx_qnpVMpDq-qhig",
  authDomain: "projectmain1-44cce.firebaseapp.com",
  databaseURL: "https://projectmain1-44cce-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "projectmain1-44cce",
  storageBucket: "projectmain1-44cce.appspot.com",
  messagingSenderId: "592837634615",
  appId: "1:592837634615:web:ca63818dd7101534dc6db2"
};
firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

self.addEventListener('push', function (event) {
  const data = event.data.json();
  const title = data.notification.title;
  const options = {
    body: data.notification.body,
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  )
});

messaging.onBackgroundMessage(function(payload) {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
