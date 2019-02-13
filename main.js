

$(function () {
    
    let socket = io();

    const urlParams = new URLSearchParams(window.location.search);
    const name = urlParams.get('name');

    $('form').submit(function(e){
      e.preventDefault(); // prevents page reloading
      socket.emit('message', {
            name:name,  
            msg:$('#m').val(),
        });
      $('#m').val('');
      return false;
    });

    $('#m').keypress(function(e){
        socket.emit('typing', {
              name:name,  
          });
      });

    socket.on('message', function(data){
        if(data.name === name){
            $('#msg-box').append( 
                $("<div class='rounded text-white p-2 mt-1 bg-secondary ml-5'>")
                .text(`${data.msg}`)
                );
        }else{
            $('#typing').text(""); //clears typing
            $('#msg-box').append( 
                $("<div class='rounded text-white p-2 mt-1 bg-primary mr-5'>")
                .text(`${data.name}: ${data.msg}`)
            );

        }
        // scroll to bottom
        $("#msg-box").scrollTop($("#msg-box")[0].scrollHeight);
      });

    socket.on('typing', function(data){
        if(data.name !== name){
            $('#typing').text(`${data.name} is typing ...`);
            // scroll to bottom
            $("#msg-box").scrollTop($("#msg-box")[0].scrollHeight);
        }
      });

  });