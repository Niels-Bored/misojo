function previousPage(filename, page){
    if(page==0){
        alert('No se puede ir más atrás')
    }else{
        page--
        window.location.href='/player/'+filename+"/"+page
    }
}

function nextPage(filename, page){
    page++
    window.location.href='/player/'+filename+"/"+page
}