var typingTimer
var donetypingInterval = 1000

//on keyup, start the countdown
$('#username').keyup(function(){
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doneTypingUsernameField, donetypingInterval);
});

//on keydown, clear the countdown
$('#username').keydown(function(){
    clearTimeout(typingTimer);
});

//user is "finished typing," do something
function doneTypingUsernameField () {
    if($('#username').val().length < 4){
         $('#username-validity').text("ID는 최소 4자 이상이어야 합니다.")
         $('#username-validity').attr('class', 'text-right text-danger' );
    }
    else {
        duplicationCheck('username', $('#username').val(), 'username-validity', '사용 가능한 ID입니다', '사용 불가능한 ID입니다 - ID중복')
    }
}

//on keyup, start the countdown
$('#email').keyup(function(){
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doneTypingEmailField, donetypingInterval);
});

//on keydown, clear the countdown
$('#email').keydown(function(){
    clearTimeout(typingTimer);
});

//user is "finished typing," do something
function doneTypingEmailField () {
        duplicationCheck('email', $('#email').val(), 'email-validity', '사용 가능한 Email입니다', '사용 불가능한 Email입니다 - 이미 가입된 Email입니다.')
}


function duplicationCheck(columnName, value, commentDOMid, validComment, invalidComment) {
    $.ajax({
        url: "/accounts/valid-check?"+columnName+"="+value,
        async : false
    }).done(function(response_message) {
        console.log(response_message)
        if(response_message === "valid"){
            $('#'+commentDOMid).text(validComment)
            $('#'+commentDOMid).attr('class', 'text-right text-success' );
        }
        else{
            $('#'+commentDOMid).text(invalidComment)
            $('#'+commentDOMid).attr('class', 'text-right text-danger' );
        }
    })
}