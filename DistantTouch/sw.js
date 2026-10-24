self.addEventListener('push', function(event) {
    // This code runs in the background even if the app is closed!
    
    // Extract the message sent from the Python server
    const payload = event.data ? event.data.text() : 'Someone is thinking of you... 💖';
    
    // Configure how the lock-screen notification looks and acts
    const options = {
        body: payload,
        icon: 'https://placehold.co/192x192/ec4899/ffffff?text=DT', // The app icon
        badge: 'https://placehold.co/72x72/ec4899/ffffff?text=DT', // The little icon in the status bar
        vibrate: [200, 100, 200, 100, 400], // A unique heartbeat vibration pattern!
        requireInteraction: true, // Keeps the notification on screen until she taps it
        data: {
            dateOfArrival: Date.now()
        }
    };

    // Tell the phone to show the notification
    event.waitUntil(
        self.registration.showNotification('Distant Touch', options)
    );
});

self.addEventListener('notificationclick', function(event) {
    // When she taps the lock-screen notification, close it...
    event.notification.close();
    
    // ...and instantly open the web app so she can send a touch back!
    event.waitUntil(
        clients.openWindow('/')
    );
});