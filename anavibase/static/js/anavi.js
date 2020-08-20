$(function(){
    $("#form-login").on("submit",function(fl){
        fl.preventDefault();
        $.ajax({
            data:new FormData(this),
            url:$(this).attr("action"),
            processData:false,
            contentType:false,
            method:"POST",
            dataType:"json",
            success:function(result){
                console.log(result)
            },
            error:function(result){

            }
        })
    });
});