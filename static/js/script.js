// Search bar and buttons
const searchButton = document.querySelector('.search-button');
const searchBar = document.querySelector('.search-bar');
const searchClose = document.querySelector('.search-close');

searchButton.addEventListener('click', () => {
    if (searchBar.classList.contains('search-open')) {
        searchBar.classList.remove('search-open');
    }
    else {
        searchBar.classList.add('search-open');
    }
})

searchClose.addEventListener('click', () => {
    searchBar.classList.remove('search-open');
})

//mobile button and mobile menu

const mobileButton = document.querySelector('.mobile-button');
const overlay = document.querySelector('.overlay');
const offCanvasOuter = document.querySelector('.offcanvas-outer');
const offCanvasMenu = document.querySelector('.offcanvas-menu');
const offCanvasClose = document.querySelector('.mobile-close');
const mobileSubMenu = document.querySelectorAll('.mobile-sub-menu');
const mobileSubMenuButton = document.querySelectorAll('.dropdown');

mobileButton.addEventListener('click', () => {
    overlay.classList.add('overlay-active');
    offCanvasMenu.classList.add('offcanvas-active');
    offCanvasOuter.style.transform = 'translate3d(320px, 0, 0)';
    offCanvasOuter.style.transition = '0.4s';
    document.body.style.overflow = 'hidden';
})

overlay.addEventListener('click', () => {
    overlay.classList.remove('overlay-active');
    offCanvasMenu.classList.remove('offcanvas-active');
    offCanvasOuter.style.transform = 'translate3d(0, 0, 0)';
    document.body.style.overflow = '';
})

offCanvasClose.addEventListener('click', () => {
    overlay.classList.remove('overlay-active');
    offCanvasMenu.classList.remove('offcanvas-active');
    offCanvasOuter.style.transform = 'translate3d(0, 0, 0)';
    document.body.style.overflow = '';
})

mobileSubMenuButton.forEach(el => {
    el.addEventListener('click', () => {
        if (el.closest('li').querySelector('.mobile-sub-menu').classList.contains('mobile-sub-menu-expaned')) {
            el.closest('li').querySelector('.mobile-sub-menu').classList.remove('mobile-sub-menu-expaned');
            }
        else {
            el.closest('li').querySelector('.mobile-sub-menu').classList.add('mobile-sub-menu-expaned');
        }
    })
})

//Sticky scrollbar

const postDetails = document.querySelector(".main-content");
const postSidebar = document.querySelector(".scrollable");
const postSidebarContent = document.querySelector(".scrollable > .aside-posts");

const controller = new ScrollMagic.Controller();
const scene = new ScrollMagic.Scene({
    triggerElement: postSidebar,
    triggerHook: 0,
    duration: getDuration
}).addTo(controller);

if (window.matchMedia("(min-width: 1020px)").matches) {
    scene.setPin(postSidebar, {pushFollowers: false});
}

// in your projects, you might want to debounce resize event for better performance
window.addEventListener("resize", () => {
    if (window.matchMedia("(min-width: 1020px)").matches) {
        scene.setPin(postSidebar, {pushFollowers: false});
    } else {
        scene.removePin(postSidebar, true);
    }
});

function getDuration() {
    return postDetails.offsetHeight - postSidebarContent.offsetHeight - 40;
}

/* begin Up button  */

function scrollTo(to, duration = 700) {
    const
        element = document.scrollingElement || document.documentElement,
        start = element.scrollTop,
        change = to - start,
        startDate = +new Date(),
        // t = current time
        // b = start value
        // c = change in value
        // d = duration
        easeInOutQuad = function (t, b, c, d) {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t + b;
            t--;
            return -c / 2 * (t * (t - 2) - 1) + b;
        },
        animateScroll = function () {
            const currentDate = +new Date();
            const currentTime = currentDate - startDate;
            element.scrollTop = parseInt(easeInOutQuad(currentTime, start, change, duration));
            if (currentTime < duration) {
                requestAnimationFrame(animateScroll);
            }
            else {
                element.scrollTop = to;
            }
        };
    animateScroll();
}

document.addEventListener('DOMContentLoaded', function () {
    let btn = document.querySelector('#toTop');
    window.addEventListener('scroll', function () {
        // Если прокрутили дальше 599px, показываем кнопку
        if (pageYOffset > 100) {
            btn.classList.add('show');
            // Иначе прячем
        } else {
            btn.classList.remove('show');
        }
    });

    // При клике прокручиываем на самый верх
    btn.onclick = function (click) {
        click.preventDefault();
        scrollTo(0, 400);
    }
});

//AJAX PAGINATION

// $.ajax({
//     type: 'GET',
//     url: '/posts-json/',
//     success: function (response) {
//         // console.log(response.data)
//         const data = response.data
//         data.map(post=> {
//             console.log(post.id)
//         })
//     },
//     error: function (error) {
//         console.log(error)
//     }
// })

//OTHER

const postContent = document.querySelector('.main-content-page');

if (!postSidebar) {
    postContent.style.flex = '0 0 100%';
    postContent.style.maxWidth = '100%';
    postContent.style.paddingRight = '0px';
}

const firstLi = document.querySelector('ul.main-blog > li');
if (firstLi) {
    firstLi.style.paddingTop = '0px';
    firstLi.style.marginTop = '0px';
    firstLi.style.border = 'none';
}

const postInfo = document.querySelector('.post-info');
    if (document.querySelector('.post-content')) {
        if (!postInfo) {
            document.querySelector('.post-content').style.flex = '0 0 100%'
            const p = document.querySelectorAll('.post-content > p').forEach(el => {
                el.style.fontSize = '1rem'
            })
        }
    }
