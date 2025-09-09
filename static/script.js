window.onload = function () {
    // Wait for the animation to finish, then display the main content
    setTimeout(function () {
        document.getElementById("home-page").style.display = "none";  // Hide home page
        document.getElementById("main-content").classList.remove("hidden");  // Show main content
    }, 2500);  // Delay to match animation time (2.5 seconds)

    // Handle button clicks
    document.getElementById("ec-btn").onclick = function () {
        alert("You selected EC. Showing EC PGs...");
        // You can redirect to a new page or display more content here
    };

    document.getElementById("cs-btn").onclick = function () {
        alert("You selected CS. Showing CS PGs...");
        // You can redirect to a new page or display more content here
    };
};
