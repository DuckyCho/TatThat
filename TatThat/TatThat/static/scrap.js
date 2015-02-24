function changeButtonStatus(){
    if($('#scrap-button').hasClass('active')){
        $('#scrap-button').removeClass('active')
        return "inactive"
    }
    else{
        $('#scrap-button').addClass('active')
        return "active"
    }
}

$('#scrap-button').click(function(){
    var curButtonStatus = changeButtonStatus()
    var url
    var comment_subtitle
    var comment_title
    var comment_desc
    if(curButtonStatus === "active"){
        url = "/scrap/addscrap/?pic_id="+$('#pic').attr('pid')
        comment_subtitle = "SCRAP SUCCESS"
        comment_title = "스크랩..성공적..!"
        comment_desc = "스크랩북으로 사진이 스크랩 되었습니다"
    }
    else{
        url = "/scrap/removescrap/?pic_id="+$('#pic').attr('pid')
        comment_subtitle = "SCRAP CANCEL SUCCESS"
        comment_title = "스크랩 취소..성공적..!"
        comment_desc = "스크랩북에서 해당 사진이 삭제되었습니다"
    }
     $.ajax({
            url: url
         }).done(function(response_message){
            $('#scrap-count').text(response_message)
            $('#comment_subtitle').text(comment_subtitle)
            $('#comment_title').text(comment_title)
            $('#comment_desc').text(comment_desc)
            $('#scrap_modal').modal('show');
         })

})

$('#non-user-scrap-button').click(function(){
    var comment_subtitle = "Login Required"
    var comment_title = "아직도 TatThat회원이 아니세요?!"
    var comment_desc = "스크랩 기능은 TatThat회원만 가능합니다. 로그인 혹은 회원가입해주세요."
    $('#comment_subtitle').text(comment_subtitle)
    $('#comment_title').text(comment_title)
    $('#comment_desc').text(comment_desc)
    $('#scrap_modal').modal('show');
})