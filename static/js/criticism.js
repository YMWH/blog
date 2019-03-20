var text = document.querySelector('.commentText');
var commentAll = document.querySelector('.commentsUl');

function usercCriticism() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // var redata = JSON.parse(xmlhttp.responseText);
            var respone = eval('(' + xmlhttp.responseText + ')');
            commentAll.innerHTML = '<li><div><div class="comment-avatar"><img src="img/avatar.png" alt="MyPassion" /></div><div class="commment-text-wrap"><div class="comment-data"><p><a href="#" class="url">' + respone[0] + '</a> <br /> <span>' + respone[2] + ' - <a href="#" class="comment-reply-link">回复</a></span></p></div><div class="comment-text">' + respone[1] + '</div></div></div></li>' + commentAll.innerHTML
        }
    };
    xmlhttp.open('POST', '/comments/course/criticism/', true);  //相当于connect
    //下面两行相当于协议包
    xmlhttp.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest'); //ajax
    xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    data = "catalog=" + text.value;
    xmlhttp.send(data);
    text.value = '';
    return false;
}