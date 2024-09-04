function showLogin() {
    document.getElementById('loginForm').style.display = 'flex';
    document.getElementById('registerForm').style.display = 'none';
    document.querySelector('.tab:nth-child(1)').classList.add('active-tab');
    document.querySelector('.tab:nth-child(2)').classList.remove('active-tab');
}

function showRegister() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'flex';
    document.querySelector('.tab:nth-child(2)').classList.add('active-tab');
    document.querySelector('.tab:nth-child(1)').classList.remove('active-tab');
}


//forgot password
function forgotPassword() {
    var username = prompt("Enter your username:");
    if (username) {
        alert("Password recovery instructions sent to your email for username: " + username);
    } else {
        alert("Username cannot be empty. Please try again.");
    }
}

//login with google
// ... (No changes in the JavaScript) ...
function loginWithGoogle() {
    alert("Login with Google clicked");
}
// document.getElementById('compareNowBtn').addEventListener('click', function() {
//     // Redirect to the compare.html page
//     window.location.href = '{{ url_for("compare") }}';
// });

function register() {
    var username = document.getElementById("registerUsername").value;
    var email = document.getElementById("registerEmail").value;
    var password = document.getElementById("registerPassword").value;

    var formData = new FormData();
    formData.append('username', username);
    formData.append('email', email);
    formData.append('password', password);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{{ url_for("register") }}', true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById("registerMessage").innerText = response.message;
        } else {
            console.error('Registration failed. Status: ' + xhr.status);
        }
    };
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.send(formData);
}
