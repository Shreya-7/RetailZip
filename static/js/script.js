window.addEventListener('resize', () => {
    changeParentHeight();
});
document.addEventListener('DOMContentLoaded', () => {

    changeParentHeight();

    // to highlight the current page on the navbar

    // get the tabId embedded in the current page
    var tabId = document.querySelector('section').dataset.tab_id;

    // remove the active class from all the navbar items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });

    const urlSearchParams = new URLSearchParams(window.location.search);
    const params = Object.fromEntries(urlSearchParams.entries());

    if (params['id']) {
        if (params['id'][0] == 'A')
            tabId = 'partners-tab';
        else
            tabId = 'services-tab';
    }

    // the home page has no embedded tabId
    if (tabId == '') {
        document.getElementById('home-tab').classList.add('active');
    }

    // assign the active class to the navbar item with the id set as tabId
    else {
        document.getElementById(tabId).classList.add('active');
    }

});

function changeParentHeight() {
    // TODO: add this script to whichever pages need this
    // don't apply the height changes for < lg windows as the overflow problem doesn't occur there.
    if (document.documentElement.clientWidth < 992) {
        return;
    }
    let childHeight = 0;
    let children = document.querySelectorAll(".card-resize");
    children.forEach(child => {
        childHeight = childHeight > child.offsetHeight ? childHeight : child.offsetHeight
    });
    let cardBodyHeight = $(".card-body").outerHeight();
    $(".card-body").css("min-height", cardBodyHeight + childHeight);
}
