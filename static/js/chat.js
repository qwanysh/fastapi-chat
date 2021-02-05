(function () {
  const form = document.getElementById('form');
  const container = document.getElementById('messages');

  const ws = new WebSocket(`ws://${location.host}/messages/`);

  const sendMessage = function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const message = formData.get('message');

    this.reset();
    ws.send(message);
  };

  const renderMessage = function (event) {
    const message = JSON.parse(event.data);
    const messageElement = document.createElement('div');
    messageElement.className = 'bg-light rounded p-2 mb-2';
    messageElement.innerHTML = `
      <p class="mb-2">${message.message}</p>
      <small class="d-block text-end">at ${message.created_at}</small>
    `;
    container.appendChild(messageElement);
  };

  form.addEventListener('submit', sendMessage);

  ws.onmessage = renderMessage;
})();