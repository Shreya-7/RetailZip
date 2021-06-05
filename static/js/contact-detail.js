document.addEventListener('DOMContentLoaded', ()=>{

    document.getElementById('contact_detail_form').onsubmit = () => {
        
        refreshAlerts();

        const alertID = 'contact-detail-alert';        
    
        var my_form = document.forms.contact_detail_form;
        var formData = new FormData(my_form);
        formData.append('type', '1'); 

        const fieldsOK = checkFields(formData, alertID);

        if(!fieldsOK) {
            return false;
        }
        
        resultAlert(alertID, "Sending consultation request...", "alert-info");
        fetch('/contact_form', {
            method: 'POST',
            body: formData
        })
        .then((response) => {

            if(response.status == 200) {
                response.json().then((response)=>{                    
                    resultAlert(alertID, response['message'], 'alert-success'); 
                    document.forms.contact_detail_form.reset();                   
                })
            }

            else {
                response.json().then((response)=>{
                    resultAlert(alertID, response['error'] , 'alert-danger');
                })
            }
        });

        return false;
    };
});

function checkFields(formData, alertID) {

    const checkboxes = ['ownership', 'vertical', 'service'];
    const checkboxField = ['Ownership Profile', 'Business Vertical', 'Retail Service'];
    var fieldsOK = true;
    var errorMessage = '';
    
    for(i=0; i<checkboxes.length; i++) {
        const checkboxName = checkboxes[i];

        if (!formData.has(checkboxName)) {

            const message = 'Please select atleast one ' + checkboxField[i];
            resultAlert(checkboxName, message, 'alert-danger', true);
            fieldsOK = false;
        }
    }

    if (/^\d{10}$/.test(formData.get('number')) == false) {
        errorMessage += 'Your phone number is invalid. ';
        fieldsOK = false;
    }

    if (formData.get('alt-number') != '' && /^\d{10}$/.test(formData.get('alt-number')) == false) {
        errorMessage += 'Your alternate number is invalid. ';
        fieldsOK = false;
    }

    if (/^\d{6}$/.test(formData.get('pincode')) == false) {
        errorMessage += 'Your pincode is invalid. ';
        fieldsOK = false;
    }

    if (!fieldsOK) {
        resultAlert(alertID, errorMessage , 'alert-danger', true);
    }

    return fieldsOK;
}

function refreshAlerts() {
    document.querySelectorAll('.alert').forEach((alert)=>{

        alert.classList.remove('alert-success');
        alert.classList.remove('alert-warning');
        alert.classList.remove('alert-danger');
        alert.classList.remove('alert-info');
        alert.innerHTML = '';
        alert.display = 'none';
    })
}

function resultAlert(alertId, message, className, checkbox=false) {

    if(!checkbox) {
        refreshAlerts();
    }

    const alert = document.getElementById(alertId);
    alert.style.display = 'block';
    alert.classList.add(className);
    alert.innerHTML = message;           
}

