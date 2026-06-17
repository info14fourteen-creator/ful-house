const mobileToggle = document.querySelector("[data-menu-toggle]");
const nav = document.querySelector("[data-nav]");

if (mobileToggle && nav) {
  mobileToggle.addEventListener("click", () => {
    const expanded = mobileToggle.getAttribute("aria-expanded") === "true";
    mobileToggle.setAttribute("aria-expanded", String(!expanded));
    nav.classList.toggle("is-open", !expanded);
  });
}

document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = new Date().getFullYear();
});

document.querySelectorAll("[data-contact-form]").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const status = form.querySelector("[data-form-status]");
    if (status) {
      status.textContent = form.dataset.success || "Request noted. Please contact us by email.";
    }
    form.reset();
  });
});
