
document.querySelectorAll("input[type='number']").forEach(input => {
    input.addEventListener("input", () => {

        if (input.value > 20) {
            input.value = 20; 
        }

        if (input.value < 0) {
            input.value = 0; 
        }
    });
});

function calculate() {

    const notes = document.querySelectorAll("input[type='number']");

    let total = 0;
    let count = 0;

    notes.forEach(input => {
        const value = parseFloat(input.value);

        if (!isNaN(value)) {
            total += value;
            count++;
        }
    });

    if (count === 0) {
        document.querySelector(".result-value").textContent = "Erreur";
        document.querySelector(".commentaire").textContent = "";
        return;
    }

    const moyenne = total / count;

   
    document.querySelector(".result-value").textContent = moyenne.toFixed(2);

    
    let message = "";

    if (moyenne < 10) {
        message = "Tu dois encore travailler, tu peux y arriver 😕💪 ! ";
    }
    else if (moyenne < 12) {
        message = "C'est Admis 🙂 !";
    }
    else if (moyenne < 14) {
        message = "C'est Assez Bien 👍 !";
    }
    else if (moyenne < 16) {
        message = "C'est Bien 😄✨ !";
    }
    else if (moyenne < 18) {
        message = "C'est Très Bien 🤩🔥 !";
    }
    else {
        message = "Excellent travail, tu es un génie 🎉🏆 !";
    }

    document.querySelector(".commentaire").textContent = message;
}