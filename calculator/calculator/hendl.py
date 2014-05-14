
    
    
    
    
    
        $(document).ready(function(){
        $('#calculate').click(function(){
            var  fruits = ["1", "2"];
            $.ajax({
                type: 'POST',
                url: '/do_something',
                data: {"fruits":JSON.stringify(fruits)},
                success: function(data){
                alert(data);
                }
            });
        });
    });