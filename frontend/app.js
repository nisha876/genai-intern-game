async function submitGuess() {
    const guess = document.getElementById("guessInput").value;
    const res = await fetch("/guess", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ guess })
    });
    const data = await res.json();
    document.getElementById("feedback").innerText = data.message;
    const scoreRes = await fetch("/score");
    const score = await scoreRes.json();
    document.getElementById("score").innerText = "Score: " + score.score;
  }
  