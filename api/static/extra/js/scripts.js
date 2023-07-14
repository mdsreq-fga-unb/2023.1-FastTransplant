function selectPage(page) {
    var links = document.getElementsByTagName('a');
    var navs = document.getElementsByTagName('li');
    for (var i = 0; i < links.length; i++) {
        links[i].classList.remove('active');
    }
    for (var i = 0; i < navs.length; i++) {
        navs[i].classList.remove('menu-open');
    }
    
    // alert("ola");
    
    switch (page) {
        case "/":
            document.getElementById("home").classList.add("active");
            break;
        case "/log/":
            document.getElementById("log").classList.add("active");
            break;
        case "/search/":
            document.getElementById("search").classList.add("active");
            break;
        case "/donators/":
            document.getElementById("donators_a").classList.add("active");
            document.getElementById("donators_list").classList.add("active");
            document.getElementById("donators_li").classList.add("menu-open");
            break;
        case "/donators/create/":
            document.getElementById("donators_a").classList.add("active");
            document.getElementById("donators_create").classList.add("active");
            document.getElementById("donators_li").classList.add("menu-open");
            break;
        case "/donators/create/pdf":
            document.getElementById("donators_a").classList.add("active");
            document.getElementById("donators_create_pdf").classList.add("active");
            document.getElementById("donators_li").classList.add("menu-open");
            break;
        case "/receivers/":
            document.getElementById("receivers_a").classList.add("active");
            document.getElementById("receivers_list").classList.add("active");
            document.getElementById("receivers_li").classList.add("menu-open");
            break;
        case "/receivers/create/":
            document.getElementById("receivers_a").classList.add("active");
            document.getElementById("receivers_create").classList.add("active");
            document.getElementById("receivers_li").classList.add("menu-open");
            break;
        case "/profile/":
            document.getElementById("users_a").classList.add("active");
            document.getElementById("profile").classList.add("active");
            document.getElementById("users_li").classList.add("menu-open");
            break;
        case "/users/":
            document.getElementById("users_a").classList.add("active");
            document.getElementById("other_users").classList.add("active");
            document.getElementById("users_li").classList.add("menu-open");
            break;
        case "/compatibility/":
            document.getElementById("compatibility_a").classList.add("active");
            document.getElementById("compatibility").classList.add("active");
            document.getElementById("compatibility_li").classList.add("menu-open");
            break;
        case "/results/":
            document.getElementById("compatibility_a").classList.add("active");
            document.getElementById("results").classList.add("active");
            document.getElementById("compatibility_li").classList.add("menu-open");
            break;
        case "/reports/":
            document.getElementById("reports").classList.add("active");
            break;
    }
}
