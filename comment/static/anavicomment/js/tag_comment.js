class AspectComment {
    constructor() {
        this.id = null;
        this.polarity = "neutral";
        this.comment = null;
        this.text=null;
    }
}

class Comment {
    constructor() {
        this.id = "";
        this.polarity = "neutral";
        this.aspects = [];
    }
}

comments={}
comments["bonjour"]= new Comment()
//alert(comments["bonjour"].polarity)

$(function(){
    $(".tag-one-comment").click(function(){
        /*alert($(this).attr("comment-id"))*/
       var  comment_id=$(this).attr("comment-id");
       var key_c="comment_"+comment_id;
        var current_comment=comments[key_c];
        var comment_polarity=$(".comment-polarity[comment-id='"+comment_id+"']:checked").val();
        //rechercher des differents aspects
        var i=0
        var nb_aspect=current_comment.aspects.length

        for(i=0;i<nb_aspect;i++){
            //on recherche l'aspect qui a l' id de l'aspect et le nom de l'aspect
            //et on recupere maintenant sa polarite
            aspect=current_comment.aspects[i]
            aspect_html=$(".aspect-polarity[aspect-id='"+aspect.id+"']:checked")
            comments[key_c].aspects[i].polarity=aspect_html.val()
        }
        comments[key_c].polarity=comment_polarity
        console.log(comments[key_c])
       var comment_to_send=JSON.stringify(new Array(comments[key_c]));

        var form_elemnt=document.getElementById("form-tag-comment");
        
        var all_comment_data=new FormData(form_elemnt);
        all_comment_data.append("comment_to_tag",comment_to_send);
       
        $.ajax({
            url:$("#form-tag-comment").attr("action"),
            method: "POST",
            data:all_comment_data,
            contentType: false,
            cache: false,
            processData: false,
            dataType: "json",
            succes:function(r){

            },
            error:function(r){

            }
        });
    });
});

