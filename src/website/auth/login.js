const form = document.querySelector("form");

const endpoint = "http://localhost:7777/login";

function setError(text) {
    document.querySelector(".error").textContent = text;
}

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const mail = document.getElementById("email");
    const pass = document.getElementById("password");

    mail.value = mail.value.trim();

    if(mail.value.length === 0) {
        setError("Email tidak boleh kosong!");
        return;
    }

    if(pass.value.length === 0) {
        setError("Password tidak boleh kosong!");
        return;
    }

    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: mail.value,
            password: pass.value
        })
    })
    .then(response => response.json())
    .then(data => {;
        if(data.status === "error") setError("Terjadi kesalahan di server");
    })
    .catch(error => {
        console.error("Request error:", error);
    });

});