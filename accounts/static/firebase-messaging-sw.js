importScripts('https://www.gstatic.com/firebasejs/9.6.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.1/firebase-messaging-compat.js');
  
var firebaseConfig = {
  apiKey: "AIzaSyCiraum9gVPXkgP3KgEXk3WMhEb64XZjZE",
  authDomain: "project-login2-6c049.firebaseapp.com",
  projectId: "project-login2-6c049",
  storageBucket: "project-login2-6c049.appspot.com",
  messagingSenderId: "865918979599",
  appId: "1:865918979599:web:b0cb8e55945a81921d9d7a",
  databaseURL: "https://project-login2-6c049-default-rtdb.europe-west1.firebasedatabase.app/",
};
firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
