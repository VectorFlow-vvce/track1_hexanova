// ===============================
// IMAGE PREVIEW (upload.html)
// ===============================
function previewImage(event) {
    const preview = document.getElementById("preview");

    if (!event.target.files[0]) return;

    preview.src = URL.createObjectURL(event.target.files[0]);
    preview.style.display = "block";
}


// ===============================
// ANALYZE BUTTON FUNCTION
// ===============================
async function analyzeCrop() {

    const fileInput = document.getElementById("fileInput");

    if (!fileInput || !fileInput.files[0]) {
        alert("Please upload an image first");
        return;
    }

    let formData = new FormData();
    formData.append("image", fileInput.files[0]);

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        // ===============================
        // STORE DATA FOR DASHBOARD
        // ===============================
        localStorage.setItem("cropResult", JSON.stringify(data));

        // ===============================
        // REDIRECT TO DASHBOARD
        // ===============================
        window.location.href = "./dashboard.html";

    } catch (error) {
        console.error("Error:", error);
        alert("Failed to analyze crop");
    }
}


// ===============================
// LOAD DATA ON DASHBOARD PAGE
// ===============================
function loadDashboard() {

    const data = JSON.parse(localStorage.getItem("cropResult"));

    if (!data) {
        console.log("No data found");
        return;
    }

    // Fill dashboard fields
    document.getElementById("disease").innerText = data.disease;
    document.getElementById("temp").innerText = data.temperature + " °C";
    document.getElementById("humidity").innerText = data.humidity + " %";
    document.getElementById("risk").innerText = data.risk;
    document.getElementById("recommendation").innerText = data.recommendation;

    let html = "";
    data.timeline.forEach(item => {
        html += `<li>${item}</li>`;
    });

    document.getElementById("timeline").innerHTML = html;
}