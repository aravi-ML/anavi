(function($){
    function display_result(result,success_location="",error_location=""){
        var icon="success";
        var pso = 'center';
        if(result["status"]==false){
            icon="error";
        }
        $.toast({
            heading: "Information",
            text: result["msg"],
            icon:icon,
            hideAfter: false,
            position:pso,
            afterHidden: function () {

            }
        });
    }

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

        //gestion des demandes de management
        $(".decide-managing").on("click",function(ert){
            ert.preventDefault();
            var askm=$(this).attr("askm-id");
            var decision=$(this).attr("decision");
            $.get("/admin/paskmanaging?askm="+askm+"&decision="+decision,{},function(result){
                display_result(result);
                $("#askmaningtr"+String(askm)).fadeOut(1000);
            },"json");
        });

        //gestion des demandes d'experts
        $(".decide-expert-apply").on("click",function(ert){
            ert.preventDefault();
            var decision=$(this).attr("decision");
            var ask_m=$(this).attr("ask_ex");
            $.ajax({
                url:"/expert/decideapply?decision="+String(decision)+"&ask="+String(ask_m),
                contentType:false,
                processData:false,
                method:"get",
                dataType:"json",
                success:function(result){
                    display_result(result);
                    $("#ask_ex"+ask_m).fadeOut();
                },
                error:function(result){
                   // window.location.reload()
                }
            });
        });


    });
})(jQuery)