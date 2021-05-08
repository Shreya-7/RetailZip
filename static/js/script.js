// to highlight the current page on the navbar

document.addEventListener('DOMContentLoaded', ()=>{

    // get the tabId embedded in the current page
    const tabId = document.querySelector('section').dataset.tab_id;

    // remove the active class from all the navbar items
    document.querySelectorAll('.nav-item').forEach(item=>{
        item.classList.remove('active');
    });

    // the home page has no embedded tabId
    if (tabId == '') {
        document.getElementById('home-tab').classList.add('active');
    }

    // assign the active class to the navbar item with the id set as tabId
    else {
        document.getElementById(tabId).classList.add('active');
    }   
    
});
