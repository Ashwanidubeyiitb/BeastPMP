const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navigation-links')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})


document.getElementById('mentor-btn').addEventListener('click', function () {
    document.querySelector('.comb_1').classList.add('comb1');
    document.querySelector('.comb_3').classList.add('comb3');
    document.querySelector('.comb_2').classList.add('comb2');
    document.querySelector('.comb_4').classList.add('comb4');
});


document.getElementById('testimonials-btn').addEventListener('click', function () {
    document.querySelector('.photo1').classList.add('photo1-animation');
    document.querySelector('.testimonial1').classList.add('testimonial1-animation');
    document.querySelector('.testimonial2').classList.add('testimonial2-animation');
    document.querySelector('.photo2').classList.add('photo2-animation');
});




// for Animation when element is in viewport

function isInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)

    );
}

// for honeycomb

const box = document.querySelector('.honey');

document.addEventListener('scroll', function () {
    const value = isInViewport(box);
    if (value) {
        document.querySelector('.comb_1').classList.add('comb1');
        document.querySelector('.comb_3').classList.add('comb3');
        document.querySelector('.comb_2').classList.add('comb2');
        document.querySelector('.comb_4').classList.add('comb4');
        // document.querySelector('.heading').classList.add('heading1');
        // document.querySelector('.explaination').classList.add('explaination1');

    }


}, {
    passive: true
});

// for testimonial section
$(document).ready(function () {
    $('#autoWidth').lightSlider({
        autoWidth: true,
        loop: true,
        onSliderLoad: function () {
            $('#autoWidth').removeClass('cS-hidden');
        }
    });
});


// for counter in about section
const about_section = document.querySelector('.hexagons-div');

document.addEventListener('scroll', function () {
    const value = isInViewport(about_section);
    if (value) {
        var department = setInterval(departmentDone, 10)
        var mentees = setInterval(menteesDone, 10)
        var mentors = setInterval(mentorsDone, 10)
        let count1 = 1;
        let count2 = 1;
        let count3 = 1;

        function departmentDone() {
            count1++;
            document.querySelector('#num1').innerHTML = count1 + '+';
            if (count1 >= 10) {
                clearInterval(department)
                document.querySelector('#num1').innerHTML = '10+';
            }
        }
        function menteesDone() {
            count2 = count2 + 10;
            document.querySelector('#num2').innerHTML = count2 + '+';
            if (count2 >= 500) {
                clearInterval(mentees)
                document.querySelector('#num2').innerHTML = '500+';
            }
        }
        function mentorsDone() {
            count3 = count3 + 5;
            document.querySelector('#num3').innerHTML = count3 + '+';
            if (count3 >= 200) {
                clearInterval(mentors)
                document.querySelector('#num3').innerHTML = '200+';
            }
        }


    }


}, {
    passive: true
});




// hovering on mentor honeycomb section
const explaination1 = document.getElementsByClassName('explaination1')[0]
const explaination2 = document.getElementsByClassName('explaination2')[0]
const explaination3 = document.getElementsByClassName('explaination3')[0]
const explaination4 = document.getElementsByClassName('explaination4')[0]

function mouseOver1() {
    explaination1.classList.add('show');
    explaination1.classList.remove('hide');
}

function mouseOut1() {
    explaination1.classList.remove('show');
    explaination1.classList.add('hide');
}
function mouseOver2() {
    explaination2.classList.add('show');
    explaination2.classList.remove('hide');
}

function mouseOut2() {
    explaination2.classList.remove('show');
    explaination2.classList.add('hide');
}
function mouseOver3() {
    explaination3.classList.add('show');
    explaination3.classList.remove('hide');
}

function mouseOut3() {
    explaination3.classList.remove('show');
    explaination3.classList.add('hide');
}
function mouseOver4() {
    explaination4.classList.add('show');
    explaination4.classList.remove('hide');
}

function mouseOut4() {
    explaination4.classList.remove('show');
    explaination4.classList.add('hide');
}
