$(document).ready(function(){
    
    var baseUrl = 'http://127.0.0.1:8000/noticias/'
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    var filter = $('#filter');
    var autorFilter = $('#autorFilter');


    $(deleteBtn).on('click', function(e){
        e.preventDefault();
        var delLink = $(this).attr('href');
        var result = confirm("Deseja deletar essa notícia?");
        if(result){
            window.location.href = delLink
        }
    });
    
    $(searchBtn).on('click', function(){
        searchForm.submit();
    })

    $(filter).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    })

    $(autorFilter).change(function(){
        var autorFilter = $(this).val();
        window.location.href = baseUrl + '?autorFilter=' + autorFilter;
    })
})