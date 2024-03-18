window.addEventListener('load', () => {
    hljs.highlightAll();
})

function cleanResponse(string) {
    let newStr = [];
    for (let match of string.matchAll(/(?:```sql\n)([\s\S]*?)(?:```)/g)) {
        let [_, matchStr] = match;
        newStr.push(matchStr);
    }
    return newStr.join('\n');
}

async function handleSubmit(e) {
    e.preventDefault();
    let loading = document.getElementById('loading');
    loading.classList.remove('d-none');

    let requirements = document.getElementById('requirements').value;
    let content_prompt = document.getElementById('contentPrompt').value;

    console.log(requirements, content_prompt);
    let dlls = await fetch('/generate_ddl', {
        method: 'POST',
        body: JSON.stringify({
            requirements,
            content_prompt
        }),
        headers: {
            'Content-type': 'application/json'
        }
    }).then(data => data.json());
    
    let {openai, claude} = dlls;

    let openaiResp = document.getElementById('openaiResponse');
    openaiResp.removeAttribute('data-highlighted');
    openaiResp.textContent = cleanResponse(openai);

    let claudeResp = document.getElementById('claudeResponse');
    claudeResp.removeAttribute('data-highlighted');
    claudeResp.textContent = cleanResponse(claude);

    document.getElementById('resultDiv').classList.remove('d-none');
    hljs.highlightAll();
    
    loading.classList.add('d-none');
}

async function copySQL(e) {
    let location = e.dataset.location;
    let ele = document.getElementById(location);
    if (ele === undefined) return;

    await navigator.clipboard.writeText(ele.textContent);
}