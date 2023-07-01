const textarea = document.getElementById('textArea');

// Row sizing
function adjustTextareaHeight(event) {
    const textarea = event.target;
    textarea.style.height = 'auto';
    textarea.style.maxHeight = '200px';
    textarea.style.height = textarea.scrollHeight + 'px';
}
textarea.addEventListener('input', adjustTextareaHeight);

// Shift Enter
textarea.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        const button = document.getElementById('submitButton');
        button.click();
        const textarea = event.target;
        textarea.style.height = 'auto';
    }
});