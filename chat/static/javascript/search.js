const searchBar = document.getElementById('searchBar');
// const userList = document.getElementById('userList');

// let sbValue = "";

searchBar.addEventListener('input', (event) => {
    sbValue = searchBar.value
    let users = document.getElementsByClassName('profile');
    for(let user of users) {
        if(user.dataset.name != undefined){
            let subSName = user.dataset.name.substring(0, sbValue.length).toLowerCase()
            let subSUsername = user.dataset.username.substring(0, sbValue.length).toLowerCase()
            if(subSName === sbValue || subSUsername=== sbValue){
                user.classList.remove("d-none");
            }else{
                user.classList.add("d-none");
            }
        }
    }
})