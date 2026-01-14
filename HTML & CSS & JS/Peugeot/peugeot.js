document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");
  const leftArrow = document.querySelector(".arrow-box");
  const rightArrow = document.querySelector(".arrow-box1");
  let currentIndex = 0;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.toggle("active", i === index);
    });
  }

  leftArrow.addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    showSlide(currentIndex);
  });

  rightArrow.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
  });

  showSlide(currentIndex);
});