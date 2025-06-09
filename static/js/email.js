
function submitEmail() {
    const email = document.getElementById('email').value;

    if (email) {    
        alert("Email registered successfully.")
    }
    else {
        alert("enter the valid email")
    }
}
window.onload = () => {
    const button = document.getElementById('button');

    button.addEventListener('mouseover', () => {
        button.textContent = "Start Learning Fast....";
    });

    button.addEventListener('mouseout', () => {
        button.textContent = "Start learning for free";
    });
}
