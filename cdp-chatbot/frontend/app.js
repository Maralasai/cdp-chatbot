function sendMessage() {
    const input = document.getElementById('chat-input').value;
    if (!input.trim()) {
        alert('Please enter a question.');
        return;
    }
    fetch('/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chat-output').innerHTML += `<p><strong>You:</strong> ${input}</p>`;
        document.getElementById('chat-output').innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;
        document.getElementById('chat-input').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Something went wrong. Please try again.');
    });
}
