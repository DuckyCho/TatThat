function initEvtListener(){
    initSwapSearchModeEvtListener()
    initSelectTagEvtListener()
    initSearchButtonEvtListener()
    activateTagButtonInSearchResult()
    var curSearchMode = document.getElementById("curSearchMode")
    document.getElementById("searchMode").style.height = curSearchMode.offsetHeight + "px"
    document.getElementById("searchButton").style.height = curSearchMode.offsetHeight + "px"
}
function activateTagButtonInSearchResult(){
    var searchBar = document.getElementById('search-bar')
    var tags = searchBar.children
    var tagCount = tags.length
    for(var i = 0 ; i < tagCount ; i++){
        var button = document.getElementById(tags[i].textContent)
        if( button != null) {
            var classAttr = button.getAttribute('class')
            addDeleteEvtListener(tags[i])
            button.setAttribute('class', classAttr + ' active')
        }
    }
}
function initSearchButtonEvtListener(){
    var searchButton = document.getElementById('searchButton')
    searchButton.addEventListener('click',redirectSearchResultPage,false)
}

function redirectSearchResultPage(){
    var curSearchMode = document.getElementById('curSearchMode')
    if(curSearchMode.textContent ==="태그검색"){
        var searchBar = document.getElementById('search-bar')
        var tagList = searchBar.children
        var length = searchBar.children.length
        var searchQuery = ""
        for(var i = 0 ; i < length ; i++){
            searchQuery += tagList[i].getAttribute('tag-name')
            if(i != length-1){
                searchQuery += '+'
            }
        }
        if(searchQuery === ""){
            alert("태그를 선택해 주세요!")
        }
        else{
            window.location.href="/search/tag/"+searchQuery
        }



    }
    else{}
}
function initSwapSearchModeEvtListener(){
    var candidate = document.getElementById('candidateSearchMode')
    if(candidate.addEventListener){
        candidate.addEventListener('click',function(event){
            swapSearchMode(event)
            swapSearchBarStatus()
        },false)
        
    }
    else if(candidate.attachEvent){
            candidate.attachEvent('onclick',function(event){
                swapSearchMode(event)
                swapSearchBarStatus()
            })
    }
}

function swapSearchMode(event){
    var replaceTarget
    var replaceStr
    if(event.target === undefined){
        replaceTarget = document.getElementById('candidateSearchMode').children[event].children[0]
        replaceStr = replaceTarget.textContent
    }
    else{
        replaceTarget = event.target
        replaceStr = event.target.textContent
    }
    var curSearchMode = document.getElementById('curSearchMode')
    var curSearchMode_text = curSearchMode.textContent
    curSearchMode.textContent = replaceStr
    replaceTarget.textContent = curSearchMode_text

}

function swapSearchBarStatus(){
        var searchBar = document.getElementById("search-bar")
        var parent = searchBar.parentElement
        var attributes = searchBar.attributes
        var attributesLength = attributes.length
        var newElement
        if(searchBar.tagName === "INPUT")
            newElement = document.createElement("div")
        else{
            newElement = document.createElement("input")
            var selectedTag = searchBar.getElementsByTagName("span")
            var selectedTagCount = selectedTag.length
            for(var i = 0 ; i < selectedTagCount ; i++){
                tagInactive(selectedTag[i].getAttribute("tag-name"))
            }
        }
        for(var i = 0 ; i < attributesLength ; i++)
            newElement.setAttribute(attributes[i].name,attributes[i].value)
        parent.insertBefore(newElement,searchBar)
        parent.removeChild(searchBar)
}

function initSelectTagEvtListener(){
    var tagButtons = document.getElementsByTagName("label")
    var tagButtonsCount = tagButtons.length
    for(var i = 0 ; i < tagButtonsCount ; i++){
        if(tagButtons[i].addEventListener){
            tagButtons[i].addEventListener('click',selectTag,false)
        }
        else if(tagButtons[i].attachEvent){
            tagButtons[i].attachEvent('click',selectTag)
        }
        
    }
}

function selectTag(event){
    var searchBar = document.getElementById("search-bar")
    var tagButton
    if(searchBar.tagName === "INPUT"){
        swapSearchMode(0)
        swapSearchBarStatus()
        searchBar = document.getElementById("search-bar")
    }
    tagButton = getTagButtonInSearchBar(searchBar,event.target.textContent)
    if(tagButton){
        searchBar.removeChild(tagButton)
    }
    else{
        tagButton = document.createElement("span")
        tagButton.setAttribute('class','btn-sm btn-danger cursor-pointer mr5 glyphicon glyphicon-remove')
        tagButton.setAttribute('tag-name',event.target.getAttribute('id'))
        tagButton.textContent = event.target.textContent
        searchBar.appendChild(tagButton)
        addDeleteEvtListener(tagButton)
    }
}
function addDeleteEvtListener(element){
    element.addEventListener('click',function(event){
        removeFromParent(event.target)
        tagInactive(event.target.getAttribute('tag-name'))
    },false)
}
function tagInactive(tagID){
    var tag = document.getElementById(tagID)
    if(tag != null)
        tag.setAttribute('class',tag.getAttribute('class').replace("active",""))
}
function removeFromParent(element){
    var parent = element.parentElement
    parent.removeChild(element)
}
function getTagButtonInSearchBar(searchBar, tagStr){
    var children = searchBar.children
    var length = children.length
    for(var i = 0 ; i < length ; i++){
        if(children[i].textContent === tagStr){
            return children[i]
        }
    }
    return false
}

initEvtListener()


