/*
* Common JavaScript
*
*/

$(function(){
    /* BOOTSTRAP COLLAPSE */
    $('.collapse').collapse({
        toggle: false
    });


    /* BOOTSTRAP.MODALS */
    $('.modal').modal({show: false});


    /* BOOTSTRAP LINKED TABS */
    $(function(){
        var
            hash = document.location.hash,
            prefix = "tab_";

        if (hash) {
            $('.nav-tabs a[href=' + hash.replace(prefix, '') + ']').tab('show');
        }

        // Change hash for page-reload
        $('.nav-tabs a').on('shown', function (e) {
            window.location.hash = e.target.hash.replace('#', '#' + prefix);
        });
    })
});
