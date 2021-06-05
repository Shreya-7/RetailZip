document.addEventListener('DOMContentLoaded', ()=>{

    document.getElementById('contact_short_form').onsubmit = () => {

        const alertID = 'contact-short-alert';        
    
        var my_form = document.forms.contact_short_form;
        var formData = new FormData(my_form);
        formData.append('type', '0');
        
        if (/^\d{10}$/.test(formData.get('number')) == false) {
            resultAlert(alertID, 'Your phone number is invalid.' , 'alert-danger');
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
                    document.forms.contact_short_form.reset();                 
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

