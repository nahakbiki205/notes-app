function addNote() {
    const input = document.getElementById("noteInput");
    const text = input.value.trim();

    if (text === "") {
        alert("Enter a note");
        return;
    }

    fetch("/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(() => {
        input.value = "";
        loadNotes();
    });
}

function loadNotes() {
    fetch("/get")
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("notesList");
        list.innerHTML = "";

        data.forEach(note => {
            const li = document.createElement("li");
            li.textContent = note;
            list.appendChild(li);
        });
    });
}

loadNotes();
