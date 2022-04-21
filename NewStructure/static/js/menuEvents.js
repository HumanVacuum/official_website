window.onload = function () {
    var checkMenu1 = document.getElementById("menu-item1");
    var checkMenu2 = document.getElementById("menu-item2");
    var checkMenu3 = document.getElementById("menu-item3");
    var checkMenuN = document.getElementById("menu-itemN");

    checkMenu1.onclick = function () {
        window.location.href = "present";
    }

    checkMenu2.onclick = function () {
        window.location.href = "history";
    }

    checkMenu3.onclick = function () {
        window.location.href = "console";
    }

    checkMenuN.onclick = function () {
        window.location.href = "setting";
    }
}