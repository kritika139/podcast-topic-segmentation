const topics = [
  "topic_01","topic_02","topic_03","topic_04","topic_05"
];

const timeline = document.getElementById("timeline");
const details = document.getElementById("details");

topics.forEach(topic => {
    const div = document.createElement("div");
    div.className = "segment";
    div.innerText = topic;

    div.onclick = async () => {
        const summary = await fetch(`../dataset/topic_summaries/${topic}_summary.txt`).then(r => r.text());
        const keywords = await fetch(`../dataset/topic_keywords/${topic}_keywords.txt`).then(r => r.text());

        details.innerHTML = `
            <h2>${topic}</h2>
            <h3>Summary</h3>
            <p>${summary}</p>
            <h3>Keywords</h3>
            <p>${keywords}</p>
        `;
    };

    timeline.appendChild(div);
});
