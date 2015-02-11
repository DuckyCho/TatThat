function initEvtListener(){
    initSwapSearchModeEvtListener()
    initSelectTagEvtListener()
    var curSearchMode = document.getElementById("curSearchMode")
    document.getElementById("searchMode").style.height = curSearchMode.offsetHeight + "px"
    document.getElementById("searchButton").style.height = curSearchMode.offsetHeight + "px"
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
        replaceStr = replaceTarget.innerText
    }
    else{
        replaceTarget = event.target
        replaceStr = event.target.innerText
    }
    var curSearchMode = document.getElementById('curSearchMode')
    var curSearchMode_text = curSearchMode.innerText
    curSearchMode.innerText = replaceStr
    replaceTarget.innerText = curSearchMode_text

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
    tagButton = getTagButtonInSearchBar(searchBar,event.target.innerText)
    if(tagButton){
        searchBar.removeChild(tagButton)
    }
    else{
        tagButton = document.createElement("span")
        tagButton.setAttribute('class','btn-sm btn-danger cursor-pointer mr5 glyphicon glyphicon-remove')
        tagButton.setAttribute('tag-name',event.target.getAttribute('id'))
        tagButton.innerText = event.target.innerText
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
        if(children[i].innerText === tagStr){
            return children[i]
        }
    }
    return false
}

initEvtListener()


