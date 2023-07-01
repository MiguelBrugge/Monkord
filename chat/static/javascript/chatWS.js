const chatId = document.currentScript.getAttribute('data-chatId');
const userId = document.currentScript.getAttribute('data-userId');

// Establish WebSocket connection
const socket = new WebSocket(`ws://${window.location.host}/ws/monkord/${chatId}/${userId}/`);
const textArea = document.getElementById('textArea');
const button = document.getElementById('submitButton');

// Connection opened
socket.addEventListener('open', (event) => {
    console.log('Connected to WebSocket');
});

// Send data to the server
const sendData = (data) => {
    if (socket.readyState === WebSocket.OPEN) {
        socket.send(data);
    } else {
        console.error('WebSocket connection is not open yet.');
    }
};

// Listen for messages from the server
socket.addEventListener('message', (event) => {
    const message = JSON.parse(event.data);
    const chatScrollingFrame = document.getElementById('chatScrollingFrame');

    // Apply bold formatting using double asterisks
    const formattedMessageText = message.text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Bold formatting
    .replace(/\*(.*?)\*/g, '<em>$1</em>') // Italic formatting
    .replace(/\#\#(.*?)\#\#/g, '<h2>$1</h2>') // H2 formatting
    .replace(/\#(.*?)\#/g, '<h1>$1</h1>'); // H1 formatting
  
  chatScrollingFrame.innerHTML += `
      <div class="d-flex gap-2 dark-hover scale-none bg-white px-4 py-2">
          <img class="rounded-circle" src="${message.writer.pfp}" width="50" height="50" alt="">
          <div style="max-width: 58vw;">
              <p class="fw-bold m-0">${message.writer.name}<span class="ms-1 text-muted text-small fw-normal font-monospace">${message.date}</span></p> 
              <p class="m-0" style="word-wrap: break-word;">${formattedMessageText}</p>
          </div>
      </div>
  `;
    chatScrollingFrame.scrollTo(0, chatScrollingFrame.scrollHeight);
    console.log('Received data:', message);
});

button.addEventListener('click', (event) => {
    sendData(textArea.value)
    textArea.value = '';
    textarea.style.height = 'auto';
})