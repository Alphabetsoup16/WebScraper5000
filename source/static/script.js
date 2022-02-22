const DOM = {
    form: document.getElementById('config-form'),
    addConfigBtn: document.getElementById('add-config')
};

const handleSubmit = (event) => {
    console.log('submit triggered');
    event.preventDefault();
}

DOM.form.onsubmit = handleSubmit;

const newConfigHtml = `
    <div class="config">
        <div class="config__group">
            <input
                type="text"
                name="config-name"
            ><label for="name-config">Name</label>
        </div>
        <div class="config__group">
            <input
                type="text"
                name="config-method"
            ><label for="method-config">Method</label>
        </div>
        <div class="config__group">
            <input
                type="text"
                name="config-arguments"
            ><label for="arguments-config">Arguments</label>
        </div>
    </div>
`;

DOM.addConfigBtn.addEventListener('click', (e) => {
    e.preventDefault()
    DOM.form.insertAdjacentHTML('afterbegin', newConfigHtml)
})