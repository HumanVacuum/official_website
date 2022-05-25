function init() {
    var url = window.location.href;
    var index = url.lastIndexOf("\/");
    var str = url.substring(index + 1,url.length);
    var now = document.getElementById(str);
    now.setAttribute("data-now","true");
    if (now.className === "menu-subItem"){
        var par = now.parentElement;
        par.setAttribute("data-hidden","false");
        (par.parentElement).firstElementChild.setAttribute("checked","true");
    }

}

function inputClicked(obj) {
    var li = obj.parentElement;
    var ul = li.lastElementChild;
    if(obj.checked){
        li.setAttribute("data-now","false");
        ul.setAttribute("data-hidden", "false");
    }else{
        li.setAttribute("data-now","true");
        ul.setAttribute("data-hidden", "true");
    }
}
