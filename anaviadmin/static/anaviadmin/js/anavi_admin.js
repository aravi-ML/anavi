(function($){
    $(function(e){
        $("#form-download-data").on("submit",function(er){
            er.preventDefault()
            var form_data=new FormData(this)
            $.ajax({
                url:$(this).attr("action"),
                data:form_data,
                contentType:false,
                cache:false,
                processData:false,
                method:"GET",
                success:function(result){
                }
            })
        });
    })
})(jQuery)