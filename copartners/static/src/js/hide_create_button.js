odoo.define('copartners.hide_create_button', function (require) {
    'use strict';

    const ListView = require('web.ListView');

    ListView.include({
        render: function (viewType, options) {
            this._super(viewType, options);
            console.log("mmarwa");
            this._hideCreateButton();
        },

        _hideCreateButton: function () {
            const createButton = this.$('.btn btn-primary o_list_button_add');

            createButton.hide();  // Hide the create button

        },
    });
});