document.addEventListener("DOMContentLoaded", function() {
    console.log("PhantomsXI Cricket Club website loaded!");

    document.querySelector(".animate-ball").classList.add("spin");
});

// Show All Images When Clicking "View All"
function showAllImages() {
    console.log("View All button clicked!"); // Debugging step

    let hiddenImages = document.querySelectorAll(".gallery-item.hidden");

    if (hiddenImages.length === 0) {
        console.log("No hidden images found!");
        return;
    }

    hiddenImages.forEach(imgDiv => {
        imgDiv.classList.remove("hidden");

        // Force image reload by appending a unique timestamp
        let imgTag = imgDiv.querySelector("img");
        let originalSrc = imgTag.getAttribute("data-src");
        if (originalSrc) {
            imgTag.src = originalSrc + "?nocache=" + new Date().getTime();
        }
    });

    // Hide the View All button after clicking
    document.getElementById("view-all-btn").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
    const seasonContainer = document.querySelector(".season-links-container");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            seasonContainer.classList.add("show-section");
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const galleryImages = document.querySelectorAll(".gallery-item img");
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");

    // Click to enlarge image
    galleryImages.forEach(img => {
        img.addEventListener("click", (event) => {
            event.stopPropagation(); // Prevent closing on image click
            lightboxImg.src = img.src;
            lightbox.classList.remove("hidden");
        });
    });

    // Click anywhere outside to close
    function closeLightbox(event) {
        if (event.target !== lightboxImg) {
            lightbox.classList.add("hidden");
        }
    }

    lightbox.addEventListener("click", closeLightbox);
});
