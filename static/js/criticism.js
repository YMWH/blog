var text = document.querySelector('.commentText');
var answer = document.querySelector('.answerText');
var commentAll = document.querySelector('.commentsUl');
var parent_reply = document.querySelectorAll('.parent');
var child_reply = document.querySelectorAll('.Child');
var parent_li = document.querySelectorAll('.parentLi');
var userReply = document.querySelectorAll('.childReply');
var allReply = document.querySelectorAll('.parentReply');
var userChildren = document.querySelectorAll('.children');
var goBack = document.querySelector('.backAll');
var userName = document.querySelector('.onLine');
var parentId = 0;
var childId = 0;
var floor = 0;
var commentsRoute = '/comments/course/criticism/';
var who = null;


parentTesting();

if(goBack){
    goBack.onclick = function () {
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
    }
}

function parentTesting() {
    if(parent_reply){
        for(var i = 0; i < parent_reply.length; i++){
            parent_reply[i].index = i;
            parent_reply[i].onclick = function () {
                console.log(this);
                console.log(this.index);
                who = this.index;
                parentId = Number(parent_reply[this.index].getAttribute("customParent"));
                console.log(parentId);
                for(var a = 0; a < allReply.length; a++){
                    allReply[a].style.display = "none";
                }
                for(var b = 0; b < userReply.length; b++){
                    userReply[b].style.display = "block";
                }
                console.log(this.index);
                console.log(parent_li[this.index]);
                userReply[0].innerHTML += parent_li[this.index].innerHTML;
                floor = 1;
                commentsRoute = '/comments/course/criticism/firstChild/';
            };
        }
    }
}

// if(child_reply){
//     for(var a = 0; a<child_reply.length; a++){
//         numChild.index = a;
//         child_reply[a].onclick = function () {
//             childId = Number(child_reply[numChild.index].getAttribute("customChild"));
//             parentId = Number(child_reply[numChild.index].getAttribute("customParent"));
//             floor = 2;
//             commentsRoute = '/comments/course/criticism/secondChild/';
//             commentFun = secondChildFun;
//         };
//     }
// }

// function secondChildFun() {
//     var xmlhttp = new XMLHttpRequest();
//     xmlhttp.onreadystatechange=function () {
//         if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
//             var respone = eval('(' + xmlhttp.responseText + ')');
//             console.log(respone)
//         }
//     };
//     xmlhttp.open('POST', route, true);  //相当于connect
//     //下面两行相当于协议包
//     xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
//     xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
//     xmlhttp.setRequestHeader( 'X-CSRFToken',document.getElementsByName("csrfmiddlewaretoken")[0].value);
//
//     data = "floor=" + floor + "&parentId=" + parentId + "&childId=" + childId + "&catalog=" + text.value;
//     xmlhttp.send(data);
//     return false;
// }

function firstChildFun(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            var respone = eval('(' + xmlhttp.responseText + ')');
            console.log(respone);
            console.log(who);
            console.log(userReply[0].childNodes);
            answer.value = "";
            for(var i = 0; i < userReply[0].childNodes.length; i++){
                if(userReply[0].childNodes[i].className){
                    console.log(userReply[0].childNodes[i].className);
                    if(userReply[0].childNodes[i].className === "children"){
                        console.log(userReply[0].childNodes[i]);
                        userReply[0].childNodes[i].innerHTML = '<li><div><div class="comment-avatar"><img src="img/avatar.png" alt="MyPassion" /></div><div class="commment-text-wrap"><div class="comment-data"><p><a href="#" class="url">' + respone[0] + '</a> <br /> <span>' + respone[2] + ' - <a href="#" class="comment-reply-link Child firstChild" customChild = "'+ respone[3] +'" customParent = "'+ respone[3] +'">回复</a></span></p></div><div class="comment-text">'+ respone[1] +'</div></div></div></li>' + userReply[0].childNodes[i].innerHTML;;
                    }
                }
            }
            userChildren[who].innerHTML = '<li><div><div class="comment-avatar"><img src="img/avatar.png" alt="MyPassion" /></div><div class="commment-text-wrap"><div class="comment-data"><p><a href="#" class="url">' + respone[0] + '</a> <br /> <span>' + respone[2] + ' - <a href="#" class="comment-reply-link Child firstChild" customChild = "'+ respone[3] +'" customParent = "'+ respone[3] +'">回复</a></span></p></div><div class="comment-text">'+ respone[1] +'</div></div></div></li>' + userChildren[who].innerHTML;
        }
    };
    xmlhttp.open('POST', commentsRoute, true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    xmlhttp.setRequestHeader( 'X-CSRFToken',document.getElementsByName("csrfmiddlewaretoken")[0].value);

    data = "floor=" + floor + "&parentId=" + parentId + "&childId=" + childId + "&catalog=" + answer.value + "&username=" + userName.innerHTML;
    xmlhttp.send(data);
    return false;
}

function usercCriticism() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // var redata = JSON.parse(xmlhttp.responseText);
            var respone = eval('(' + xmlhttp.responseText + ')');
            text.value = "";
            commentAll.innerHTML = '<li  class="parentLi"><div><div class="comment-avatar"><img src="img/avatar.png" alt="MyPassion" /></div><div class="commment-text-wrap"><div class="comment-data"><p><a href="#" class="url">' + respone[0] + '</a> <br /> <span>' + respone[2] + ' - <a href="#" class="comment-reply-link parent" customParent = '+ respone[3] +'>回复</a></span></p></div><div class="comment-text">' + respone[1] + '</div></div></div><ul class = "children"></ul></li>' + commentAll.innerHTML
            parent_reply = document.querySelectorAll('.parent');
            parent_li = document.querySelectorAll('.parentLi');
            parentTesting();
        }
    };
    xmlhttp.open('POST', commentsRoute, true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    xmlhttp.setRequestHeader( 'X-CSRFToken',document.getElementsByName("csrfmiddlewaretoken")[0].value);

    data = "floor=" + floor + "&parentId=" + parentId + "&childId=" + childId + "&catalog=" + text.value + "&username=" + userName.innerHTML;
    xmlhttp.send(data);
    return false;
}

