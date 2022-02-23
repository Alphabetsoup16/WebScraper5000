const DOM = {
    form: document.getElementById('config-form'),
    configGenPoint: document.getElementById('config-gen'),
    configUrl: document.getElementById('config-url'),
    addConfigBtn: document.getElementById('add-config'),
    configList: document.getElementsByClassName('config')
};

const saveTemplateAsFile = (filename, dataObjToWrite) => {
    const blob = new Blob([JSON.stringify(dataObjToWrite)], { type: "text/json" });
    const link = document.createElement("a");

    link.download = filename;
    link.href = window.URL.createObjectURL(blob);
    link.dataset.downloadurl = ["text/json", link.download, link.href].join(":");

    const evt = new MouseEvent("click", {
        view: window,
        bubbles: true,
        cancelable: true,
    });

    link.dispatchEvent(evt);
    link.remove()
};

const handleSubmit = async (event) => {
    event.preventDefault();

    const configObjects = Array.from(DOM.configList).map(configGroup => {
        const configField = Array.from(configGroup.getElementsByTagName('input'));
        const configObj = {
            name: configField[0].value,
            method: configField[1].value,
            arguments: JSON.parse(configField[2].value)
        }
        return configObj
    });

    const configBody = {
        url: DOM.configUrl.value,
        configs: configObjects
    };

    try {
        const res = await fetch('http://127.0.0.1:8000/api/v1/scrape/', {
            method: 'post',
            headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
            },
            body: JSON.stringify(configBody)
        });

        const scrapedRes = await res.json();

        if (scrapedRes) {
            saveTemplateAsFile("scrape.json", scrapedRes);
        }
    } catch(err) {
        console.log(err)
    };
};

DOM.form.onsubmit = handleSubmit;

const newConfigHtml = `
    <div class="config">
        <div class="config__group">
            <input
                type="text"
                name="config-name"
                class="config-field"
            ><label for="name-config">Name</label>
        </div>
        <div class="config__group">
            <input
                type="text"
                name="config-method"
                class="config-field"
            ><label for="method-config">Method</label>
        </div>
        <div class="config__group">
            <input
                type="text"
                name="config-arguments"
                class="config-field"
            ><label for="arguments-config">Arguments</label>
        </div>
    </div>
`;

DOM.addConfigBtn.addEventListener('click', (e) => {
    e.preventDefault()
    DOM.configGenPoint.insertAdjacentHTML('beforeend', newConfigHtml)
})