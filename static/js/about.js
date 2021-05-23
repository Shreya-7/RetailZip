document.addEventListener('DOMContentLoaded', ()=>{

    var counter = 0;
    document.querySelectorAll('#values-and-help h4').forEach(heading => {

        if(counter%2==0) {
            heading.classList.add('color-blue');
        }
        else {
            heading.classList.add('color-red');
        }

        counter++;
    });
});