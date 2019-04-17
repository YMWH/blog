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
var overplusDate = document.querySelector('.overplus');
var verificationText = document.querySelector('.verificationCode');
var userReply = document.querySelectorAll('.childReply');
var allReply = document.querySelectorAll('.parentReply');
var route = '/comments/login/';
var date = 0;
var newDate = new Date();
var verifyCode = '';
var parentId = 0;
var childId = 0;
var floor = 0;
var who = null;



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
    verifyCode = new GVerify("verification_img");
};
back_login.onclick = function () {
    register_Form.style.display = "none";
    login_Form.style.display = "block";
    route = '/comments/login/';
};

login.onclick = function (e) {
    e = e || event;
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
                console.log(onLine.innerHTML);
                onLine.innerHTML = "";
                console.log(onLine.innerHTML);
                parentId = 0;
                childId = 0;
                floor = 0;
                who = null;
                userReply[0].innerHTML = '<h5 class="line"><span>他在听着呢</span></h5>';
                for(var i = 0; i < userReply.length; i++){
                    userReply[i].style.display = "none";
                }
                for(var a = 0; a < allReply.length; a++){
                    allReply[a].style.display = "block";
                }
                login.innerHTML = '<a href="#" class="offLine">登录</a>';
                funCancel()
            }
        }
    };


    xmlhttp.open('POST', '/comments/cancel/', true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    xmlhttp.setRequestHeader( 'X-CSRFToken',document.getElementsByName("csrfmiddlewaretoken")[0].value);
    var userName = nodeFirst[i].innerHTML;
    if(!userName){
        userName = nodeFirst[i+1].innerHTML;
    }
    data = "name=" + userName;
    xmlhttp.send(data);
    return false;
}

function submitregister() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            var respone = eval('(' + xmlhttp.responseText + ')');

            var reglogin = /register/;
            if(reglogin.test(respone[0])){
                switch (respone[1]) {
                    case 0:
                        overplusDate.innerHTML = "账号已经存在，请重新注册";
                        break;
                    case -1:
                        switch (respone[2]) {
                            case 0:
                                overplusDate.innerHTML = "该邮箱已经注册过，请用其他邮箱注册";
                                break;
                        }
                        break;
                    case 1:
                        overplusDate.innerHTML = "可喜可贺可喜可贺，不用当哑巴了！";
                        setTimeout(auto, 3000);
                        function auto() {
                            register_Form.style.display = "none";
                            login_Form.style.display = "block";
                            route = '/comments/login/';
                            registerName.innerHTML = "";
                            registerPwd.innerHTML = "";
                            userAginPwd.innerHTML = "";
                            userMail.innerHTML = "";
                            verificationText.innerHTML = "";
                            overplusDate.innerHTML = "";
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
    xmlhttp.setRequestHeader( 'X-CSRFToken',document.getElementsByName("csrfmiddlewaretoken")[0].value);

    var regRoute = /register/;
    if(regRoute.test(route)){
        var res = verifyCode.validate(verificationText.value);
        if(res){
            overplusDate.innerHTML = "";
            if ((registerPwd.value === userAginPwd.value) && checking()){
                userTips.innerHTML = '';
                data = "csrfmiddlewaretoken"+document.getElementsByName("csrfmiddlewaretoken")[0].value + "&userName=" + registerName.value + "&password=" + registerPwd.value + "&mailbox=" + userMail.value;
                xmlhttp.send(data);
            }else{
                userTips.innerHTML = '第一次输入的密码和第二次输入的密码不相等';
            }
        }else{
            overplusDate.innerHTML = '验证码错误';
        }
    }
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
                        setTimeout(auto, 3000);
                        var reg = /login=True/;
                        if(reg.test(document.cookie) && respone[2]){
                            userCue.innerHTML = "告诉你一个好消息，登录成功了，你可以为所欲为啦⬅_⬅";
                            setTimeout(auto, 3000);
                            function auto() {
                                register_Form.style.display = "none";
                                login_Form.style.display = "block";
                                loginBox.className = 'cover';
                                loginName.value = "";
                                loginPwd.value = "";
                                userCue.innerHTML = "";
                                try{
                                    hideDiscuss.style.display = "none";
                                    for(var i = 0; i < Discuss.length; i++){
                                        Discuss[i].style.display = "block"
                                    }
                                }catch (e) {
                                    console.log("欢迎来到影梦无痕的个人网站")
                                }
                                finally {
                                    login.innerHTML = '<a href="#" class="onLine">' + respone[3] + '</a> <a href="#" class="cancel">注销</a>';
                                    console.log(typeof respone[3]);
                                    console.log(onLine ===null);
                                    if(onLine !== null){
                                        onLine.innerHTML = respone[3];
                                    }

                                }
                            }
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
    xmlhttp.setRequestHeader( 'X-CSRFToken',document.getElementsByName("csrfmiddlewaretoken")[0].value);

    var regRoute = /login/;
    if(regRoute.test(route) && checking()){
        data = "userName="+loginName.value + "&" + "password="+loginPwd.value;
        xmlhttp.send(data);
    }
    return false;
}
