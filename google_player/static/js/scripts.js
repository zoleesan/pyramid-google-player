$(document).ready(function(){

    $('.render-audio').click(function(){
        audioContainer = $(this).parent().find('.audio-player');

        if(audioContainer.hasClass('empty')) {
            songUrl = $(this).attr('data-songurl');

            audioElement = "<audio style=\"display:none\" class=\"full-width\" controls=\"controls\"> \
                                <source src=\"" + songUrl + "\" type=\"audio/mpeg\"> \
                            </audio>";

            audioContainer.append(audioElement).toggleClass('empty');
            audioContainer.find('audio').fadeIn('fast');
            $(this).find('i').toggleClass('icon-play').toggleClass('icon-stop');
        } else {
            audioContainer.html('').toggleClass('empty');
            $(this).find('i').toggleClass('icon-play').toggleClass('icon-stop');
        }
    });

});