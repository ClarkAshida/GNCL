$(document).ready(function(){

    var baseUrl = 'http://127.0.0.1:8000/funcionarios/funcionarios/'
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter')

    $(deleteBtn).on('click', function(e){
        e.preventDefault();
        var delLink = $(this).attr('href');
        var result = confirm("Deseja deletar esse funcionário?");
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
})