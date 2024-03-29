document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("startButton");
    button.addEventListener("click", startTest);

    function startTest() {
        const container = document.querySelector(".container");
        container.classList.add("animation-target", "show");
        alert("Тест начался! Удачи!");
        // Здесь можно добавить логику теста
    }
});
