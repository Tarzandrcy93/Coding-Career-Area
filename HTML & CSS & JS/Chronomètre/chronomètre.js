let timer;
let isRunning = false;
let startTime = 0;
let elapsedBeforePause = 0;

const display = document.getElementById("display");
const startBtn = document.getElementById("startBtn");
const pauseBtn = document.getElementById("pauseBtn");
const resetBtn = document.getElementById("resetBtn");

function updateDisplay() {
  const now = Date.now();
  const elapsed = now - startTime + elapsedBeforePause;

  const hrs = String(Math.floor(elapsed / 3600000)).padStart(2, '0');
  const mins = String(Math.floor((elapsed % 3600000) / 60000)).padStart(2, '0');
  const secs = String(Math.floor((elapsed % 60000) / 1000)).padStart(2, '0');
  const ms = String(elapsed % 1000).padStart(3, '0');

  display.textContent = `${hrs}:${mins}:${secs}:${ms}`;
}

startBtn.addEventListener("click", () => {
  if (!isRunning) {
    startTime = Date.now();
    timer = setInterval(updateDisplay, 10);
    isRunning = true;
  }
});

pauseBtn.addEventListener("click", () => {
  if (isRunning) {
    clearInterval(timer);
    elapsedBeforePause += Date.now() - startTime;
    isRunning = false;
  }
});

resetBtn.addEventListener("click", () => {
  clearInterval(timer);
  isRunning = false;
  startTime = 0;
  elapsedBeforePause = 0;
  display.textContent = "00:00:00:000";
});