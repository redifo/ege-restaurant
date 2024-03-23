function goBack() {
    window.history.back();
}

$("#copyright").text(new Date().getFullYear());

document.addEventListener("DOMContentLoaded", function () {
    // Update placeholders and labels
    document.getElementsByName("username")[0].setAttribute("placeholder", "Name");
    
    document.querySelector("label[for='id_username']").textContent = "Name:";
    
});