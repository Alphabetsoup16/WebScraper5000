const DOM = {
    form: document.getElementById('config-form'),
    configGenPoint: document.getElementById('config-gen'),
    addConfigBtn: document.getElementById('add-config')
};

const handleSubmit = (event) => {
    console.log('submit triggered');
    event.preventDefault();
};

DOM.form.onsubmit = handleSubmit;

let idCount = 0;

const newConfigHtml = (count) => {
    return (
        `
            <div class="config" id="config-item-${count}">
                <div class="config__group">
                    <input
                        type="text"
                        name="config-name"
                        id="config-name-${count}"
                    ><label for="name-config">Name</label>
                </div>
                <div class="config__group">
                    <input
                        type="text"
                        name="config-method"
                        id="config-method-${count}"
                    ><label for="method-config">Method</label>
                </div>
                <div class="config__group">
                    <input
                        type="text"
                        name="config-arguments"
                        id="config-arguments-${count}"
                    ><label for="arguments-config">Arguments</label>
                </div>
            </div>
        `
    )
}

DOM.addConfigBtn.addEventListener('click', (e) => {
    e.preventDefault()
    DOM.configGenPoint.insertAdjacentHTML('beforeend', newConfigHtml(idCount))
    idCount++;
})