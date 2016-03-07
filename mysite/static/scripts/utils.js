var Utils = (function(){

    return {

        /**
         * Displays the main alert message.
         * @param text
         */
        alertShow: function(text) {
            $('#alert-msg-text').text(text);
            $('#alert-msg').show();
        },


        /**
         * Displays alert message in the edit modal dialog.
         * @param text
         */
        alertEditModalShow: function(text) {
            $('#alert-edit-modal-text').text(text);
            $('#alert-edit-modal').show();
        },

        /**
         * Closes alert message in the edit modal dialog.
         */
        alertEditModalClose: function() {
            $('#alert-edit-modal-text').text('');
            $('#alert-edit-modal').hide();
        },

        /**
         * Displays alert message in the delete modal dialog.
         * @param text
         */
        alertDeleteModalShow: function(text) {
            $('#alert-delete-modal-text').text(text);
            $('#alert-delete-modal').show();
        },

        /**
         * Closes alert message in the edit modal dialog.
         */
        alertDeleteModalClose: function() {
            $('#alert-delete-modal-text').text('');
            $('#alert-delete-modal').hide();
        },

        /**
         * Displays success message.
         * @param text
         */
        successShow: function(text) {
            $('#success-msg-text').text(text);
            $('#success-msg').show();
        },



    };

})();