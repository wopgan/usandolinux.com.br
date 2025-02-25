/* document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    menuToggle.addEventListener("click", function () {
        navMenu.classList.toggle("show");
    });
});
 */

document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");
    const navbar = document.querySelector(".navbar");

    // Alternar menu ao clicar no botão
    menuToggle.addEventListener("click", function () {
        navMenu.classList.toggle("show");
        document.body.classList.toggle("menu-open"); // Ativar fundo desfocado
    });

    // Fechar menu ao clicar em um item (mobile)
    document.querySelectorAll(".nav-menu a").forEach(item => {
        item.addEventListener("click", () => {
            navMenu.classList.remove("show");
            document.body.classList.remove("menu-open");
        });
    });

    // Efeito de rolagem para navbar
    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
});
