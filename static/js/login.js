var login = document.querySelector("#login");
var loginBox = document.querySelector('.cover');
var loginExit = document.querySelector('.exit');
var login_Form = document.querySelector('.loginForm');
var register_Form = document.querySelector('.registerForm');
var back_login = document.querySelector('.back');
var go_register = document.querySelector('.Go');
var loginName = document.querySelector('#id_username');
var loginPwd = document.querySelector('#id_password');
var registerName = document.querySelector('#register_username');
var registerPwd = document.querySelector('#register_password');
var userAginPwd = document.querySelector('#again_password');
var userMail = document.querySelector('#mailbox');
var userTips = document.querySelector('.tips');
var userCue = document.querySelector('.cue');
var Discuss = document.querySelectorAll('.discuss');
var hideDiscuss = document.querySelector('.loginPrompt');
var offLine = document.querySelector('.offLine');
var onLine = document.querySelector('.onLine');
var loginA = login.querySelector('a');
var cancel = login.querySelector('.cancel');
var route = '/comments/login/';

if(loginA === onLine){
    funLogin()
}else if(loginA === offLine){
    funCancel()
}


loginExit.onclick = function(){
    register_Form.style.display = "none";
    login_Form.style.display = "block";
    loginBox.className = 'cover';
};
go_register.onclick = function () {
    login_Form.style.display = "none";
    register_Form.style.display = "block";
    route = '/comments/register/';
};
back_login.onclick = function () {
    register_Form.style.display = "none";
    login_Form.style.display = "block";
    route = '/comments/login/';
};

login.onclick = function (e) {
    e = e || event;
    console.log(e.target);
    if(e.target.className === "offLine"){
        loginBox.className += ' coverOut';
    }else if(e.target.className === "cancel"){
        var parent = e.target.parentNode;
        var nodeFirst = parent.childNodes;
        for(var i = 0;i<nodeFirst.length;i++){
            if(nodeFirst[i].nodeName = "A"){
                userCancel(nodeFirst, i);
                break;
            }
        }
    }
};

// try{
//     offLine.onclick = function(){
//         loginBox.className += ' coverOut';
//     };
// }catch (e) {
//     cancel.onclick = function(){
//         userCancel()
//     };
// }


function funCancel() {
    try{
        hideDiscuss.style.display = "block";
        for(var i = 0; i < Discuss.length; i++){
            Discuss[i].style.display = "none"
        }
    }catch (e) {
        return
    }
}

function funLogin() {
    try{
        hideDiscuss.style.display = "none";
        for(var i = 0; i < Discuss.length; i++){
            Discuss[i].style.display = "block"
        }
    }catch (e) {
        return
    }
}

function checking() {
    var regName = /^\w{3,10}$/;
    var regPwd = /^\w{3,10}$/;
    var regMail = /^\w+@[0-9a-zA-Z]{2,}(\.[a-zA-Z]{2,}){1,2}$/;
    var regRoute = /login/;
    if(regRoute.test(route)){
        if(regName.test(loginName.value) && regPwd.test(loginPwd.value)){
            return true
        }else{
            return false
        }
    }else{
        if(regName.test(registerName.value) && regPwd.test(registerPwd.value) && regMail.test(userMail.value)){
            return true
        }else{
            return false
        }
    }
}

function userCancel(nodeFirst, i) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // var redata = JSON.parse(xmlhttp.responseText);
            var respone = eval('(' + xmlhttp.responseText + ')');
            if(respone[0] === 0){
                login.innerHTML = '<a href="#" class="offLine">登录</a>';
                funCancel()
            }
        }
    };


    xmlhttp.open('POST', '/comments/cancel/', true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    var userName = nodeFirst[i].innerHTML;
    if(!userName){
        userName = nodeFirst[i+1].innerHTML;
    }
    data = "name=" + userName;
    xmlhttp.send(data);

    return false;
}

function submitlogin() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // var redata = JSON.parse(xmlhttp.responseText);
            var respone = eval('(' + xmlhttp.responseText + ')');
            var reglogin = /login/;
            if(reglogin.test(respone[0])){
                switch (respone[1]) {
                    case 0:
                        userCue.innerHTML = "亲爱的，你还没注册哦，点一下上面就有发言权了哦⬅_⬅";
                        break;
                    case -1:
                        userCue.innerHTML = "你输入的密码我这里没有记载欸，应该是你弄错了吧";
                        break;
                    case -2:
                        userCue.innerHTML = "你已经在线了啊，还登录干嘛？要上天还是咋滴？";
                        break;
                    case 1:
                        userCue.innerHTML = "告诉你一个好消息，登录成功了，你可以为所欲为啦⬅_⬅";
                        setTimeout(auto, 3000);
                        function auto() {
                            register_Form.style.display = "none";
                            login_Form.style.display = "block";
                            loginBox.className = 'cover';
                            hideDiscuss.style.display = "none";
                            loginName.value = "";
                            loginPwd.value = "";
                            userCue.innerHTML = "";
                            for(var i = 0; i < Discuss.length; i++){
                                Discuss[i].style.display = "block"
                            }
                            login.innerHTML = '<a href="#" class="onLine">' + respone[3] + '</a> <a href="#" class="cancel">注销</a>';
                        }
                        break;
                }
            }
        }
    };
    xmlhttp.open('POST', route, true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');

    var regRoute = /login/;
    if(regRoute.test(route) && checking()){
        data = "userName="+loginName.value+"&"+"password="+loginPwd.value;
        xmlhttp.send(data);
    }
    return false;
}

function submitregister() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // var redata = JSON.parse(xmlhttp.responseText);
            var respone = eval('(' + xmlhttp.responseText + ')');
            console.log(respone);
            console.log(respone[0]);
            console.log(typeof(respone));
        }
    };
    xmlhttp.open('POST', route, true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');


    var regRoute = /register/;
    if(regRoute.test(route)){
        console.log(checking());
        if ((registerPwd.value === userAginPwd.value) && checking()){
            userTips.innerHTML = '';
            data = "userName=" + registerName.value + "&" + "password=" + registerPwd.value + "&" + "mailbox=" + userMail.value;
            xmlhttp.send(data);
        }else{
            userTips.innerHTML = '第一次输入的密码和第二次输入的密码不相等';
        }
    }
    return false;
}
