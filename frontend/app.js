document.addEventListener("DOMContentLoaded", function() {
    fetch("http://127.0.0.1:5000/")
        .then(response => response.json())
        .then(data => {
            document.getElementById("message").textContent = data.message;
        })
        .catch(error => console.error("API çağrısı başarısız:", error));
});
