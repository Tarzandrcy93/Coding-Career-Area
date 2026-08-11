let count = 0;

document.getElementById("box").addEventListener("click", function() {
    count++;
    this.textContent = "Tu as cliqué " + count + " fois";
});