(function($){$(function(){
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

    function find_country_town(){
        var country=$("#hotel-country").val().trim()
        $.get("/country/get-country-cities?country="+country,{},function(result){
            $("#hotel-town").html("")
            var new_html=""
            var length=result["data"].length
            for(var i=0;i<length;i++){
                new_html+="<option value='"+result["data"][i]['id']+"'>"+result["data"][i]['name']+"</option>"
            }
            $("#hotel-town").html(new_html)
        },"JSON");
    }
    try{
        find_country_town();
    }
    catch(error){}
    
    
    $("#hotel-country").change(function(){
        find_country_town()
    });
    //code pour ajouiter un hotel depuis un utlisateur

    $("#add-hotel-from-user").on("submit",function(ert){
        ert.preventDefault()
        var form_data=new FormData(this)
        $.ajax({
            data:form_data,
            dataType:"json",
            processData:false,
            method:"POST",
            contentType:false,
            url:$(this).attr("action"),
            success:function(result){
                display_result(result)
            },
            error:function(result){

            }

        })
    });
    //fin ajout hotel depuis un utilisateur
function charge_find_hotel_ask(){
    var value=$("#find-hotel-ask").val().trim()
    if(hotel_information[value]!=undefined){
        $("#hfind-name").text(hotel_information[value]["name"])
        $("#hfind-place").text(hotel_information[value]["place"])
    }
    else{
        $("#hfind-name").text("")
        $("#hfind-place").text("")
    }
}

$("#find-hotel-ask").on("input click change keyup focus keydown",function(){
    charge_find_hotel_ask()
});
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
                var icon="success"
                var pso = 'center';
                if(result["status"]==false){
                    icon="error"
                }
                else if(result["status"]==true){
                    window.location.replace(home_url)
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


            },
            error:function(result){

            }
        })
    });

    //gestion du formulaire de demande a adminsiter un hotel
    $("#form-ask-managing-hotel").on("submit",function(ert){
        ert.preventDefault()
        $.ajax({
            url:$(this).attr("action"),
            data:new FormData(this),
            processData:false,
            dataType:"json",
            contentType:false,
            method:"post",
            success:function(result){
                display_result(result)
            }
        })
    });


    
}); })(jQuery) 