document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("startButton").addEventListener("click", function() {

            document.getElementById("startButton").style.transform = "scale(0.9)";
            document.getElementById("startButton").style.transition = "transform 0.2s ease";
            document.getElementById("startButton").classList.add("shrink");

            setTimeout(function() {
                window.location.href = "assessment";
            }, 200);
        });
});
