const open_button = document.querySelector('.open_button')
const close_button = document.querySelector('.close_button')


// when the open button is clicked
open_button.addEventListener("click", () => {


    // we will render the blocks before the navbar width is set

    document.getElementById('Chat-Groups').style.display = 'block';
    document.getElementById('Chat-Groups').style.visibility = 'visible';

    document.getElementById('searchbox').style.display = 'block';
    document.getElementById('searchbox').style.visibility = 'visible';



    document.getElementById('room-name').style.display = 'none';
    document.getElementById('room-name').style.visibility = 'hidden';


    document.getElementById('message_input_form').style.display = 'none';

    const close_button = document.getElementById('close_button');
    close_button.style['display'] = 'flex';
    close_button.style['visibility'] = 'visible';

    const open_button = document.getElementById('open_button');
    open_button.style['display'] = 'none';
    open_button.style['visibility'] = 'hidden';

    const nav = document.getElementById('left-navbar');
    nav.style['width'] = '100%';

    // for rendering the groups list
    var link_text = document.querySelectorAll('.link-text');
    for (var i = 0; i < link_text.length; i++) {
        link_text[i].style.visibility = 'visible';
        link_text[i].style.display = 'block';
    }


})


close_button.addEventListener("click", () => {




    // we will render the blocks before the navbar width is set
    document.getElementById('Chat-Groups').style.display = 'none';
    document.getElementById('Chat-Groups').style.visibility = 'hidden';

    document.getElementById('searchbox').style.display = 'none';
    document.getElementById('searchbox').style.visibility = 'hidden';




    document.getElementById('room-name').style.display = 'flex';
    document.getElementById('room-name').style.visibility = 'visible';

    document.getElementById('message_input_form').style.display = 'block';
    document.getElementById('message_input_form').style.visibility = 'visible';


    const close_button = document.getElementById('close_button');
    close_button.style['display'] = 'none';
    close_button.style['visibility'] = 'hidden';



    const open_button = document.getElementById('open_button');
    open_button.style['display'] = 'flex';
    open_button.style['visibility'] = 'visible';


    const nav = document.getElementById('left-navbar');
    nav.style['width'] = '0%';


    // for rendering the groups list
    var link_text = document.querySelectorAll('.link-text');
    for (var i = 0; i < link_text.length; i++) {
        link_text[i].style.visibility = 'hidden';
        link_text[i].style.display = 'none';
    }



})

const option_button = document.querySelector('.option')
option_button.addEventListener('click', ()=>{
    
})


function myFunction(x) {
    if (x.matches) { // If media query matches
        console.log(x)
        const list = document.querySelector('.left-navbar-nav')
        list.addEventListener('click', () => {

            console.log('list is clicked')
            

        })

    } else {
        // document.body.style.backgroundColor = "pink";
        console.log('sorry')
    }
}

var x = window.matchMedia("(min-width:320px) and (orientation:portrait)")
myFunction(x) // Call listener function at run time
x.addListener(myFunction) // Attach listener function on state changes 