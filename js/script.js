document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get username and password from input fields
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Fetch users from JSON file (Assuming asynchronous fetch)
    fetch('./json/user.json')
        .then(response => response.json())
        .then(data => {
            // Check if username and password match any user in JSON data
            var users = data.users;
            var validUser = users.find(user => user.username === username && user.password === password);
            
            if (validUser) {
                // Successful login
                document.getElementById('message').innerHTML = 'Login successful!';
                // Redirect to coding.html
                window.location.href = 'coding.html';
            } else {
                // Failed login
                document.getElementById('message').innerHTML = 'Invalid username or password. Please try again.';
            }
        })
        .catch(error => {
            console.error('Error fetching users:', error);
            document.getElementById('message').innerHTML = 'Error fetching users. Please try again later.';
        });
});
