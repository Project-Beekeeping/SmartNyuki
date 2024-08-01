document.addEventListener('DOMContentLoaded', () => {
    const helpBtn = document.getElementById('loginBtn');
    loginBtn.addEventListener('click', () => {
        window.location.href = 'signin.html';
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const helpBtn = document.getElementById('signupBtn');
    signupBtn.addEventListener('click', () => {
        window.location.href = 'sign up.html';
    });
});




document.addEventListener('DOMContentLoaded', () => {
    const helpBtn = document.getElementById('helpBtn');
    helpBtn.addEventListener('click', () => {
        window.location.href = 'help.html';
    });
});