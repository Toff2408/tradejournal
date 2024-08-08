window.onload = function() {
    setTimeout(function() {
        const messageElement = document.getElementById('message');
        if (messageElement) {
            messageElement.style.display = 'none';
        }
    }, 5000); // Timeout set to 5 seconds (5000 milliseconds)
}

document.addEventListener('DOMContentLoaded', function() {
    const modalButtons = document.querySelectorAll('.modalButton');
    const closeButtons = document.querySelectorAll('.closeButton');
    const body = document.body;

    modalButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal-id');
            const modal = document.getElementById(modalId);
            modal.style.display = 'block';
            body.classList.remove('blurred');
        });
    });

    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.modal');
            modal.style.display = 'none';
            body.classList.remove('blurred');
        });
    });

    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            event.target.style.display = 'none';
            body.classList.remove('blurred');
        }
    });
});



// const modalButton = document.getElementById('modalButton');
// const modal = document.getElementById('myModal');
// const closeButton = document.getElementById('closeButton');
// const body = document.body;

// function openModal() {
//     modal.style.display = 'block';
//     body.classList.remove('blurred');
// }

// function closeModal() {
//     modal.style.display = 'none';
//     body.classList.remove('blurred');
// }

// modalButton.addEventListener('click', openModal);
// closeButton.addEventListener('click', closeModal);

// window.addEventListener('click', function(event) {
//     if (event.target == modal) {
//         closeModal();
//     }
// });



