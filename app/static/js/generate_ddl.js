const AVAILABLE_MODELS = ['openai', 'claude']

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

    let prompt = document.getElementById('requirements').value;
    let content_prompt = document.getElementById('contentPrompt').value;

    console.log(requirements, content_prompt);
    for (const model of AVAILABLE_MODELS) {
        let dlls = fetch('/response', {
            method: 'POST',
            body: JSON.stringify({
                model,
                prompt,
                content_prompt
            }),
            headers: {
                'Content-type': 'application/json'
            }
        }).then(d => d.json())
          .then(response => {
            if (response.success === false) {
                console.log('Error: ', response.message)
            }
            console.log(response);
            let respCode = document.getElementById(`${model}Response`);
            respCode.removeAttribute('data-highlighted');
            respCode.textContent = cleanResponse(response.message);
        })
        .catch(error => {
            console.log(error);
            loading.classList.add('d-none');
        });
    }

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