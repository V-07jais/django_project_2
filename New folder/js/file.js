// script.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("Sandbox project JS active ✅");

    // ---------- Signup/Login Page ----------
    const loginForm = document.querySelector("#loginForm");
    const signupForm = document.querySelector("#signupForm");

    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Login submitted (backend will handle later).");
        });
    }

    if (signupForm) {
        signupForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Signup submitted (backend will handle later).");
        });
    }

    // ---------- Add Project Page ----------
    const projectForm = document.querySelector("#projectForm");

    if (projectForm) {
        projectForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Project added (backend will handle later).");
        });
    }

    // ---------- Profile Page ----------
    const editBtn = document.querySelector("#editProfileBtn");

    if (editBtn) {
        editBtn.addEventListener("click", () => {
            alert("Profile edit coming soon.");
        });
    }
});
