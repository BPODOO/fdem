odoo.define('iotRealTime_extend', function (require) {
    'use strict';

    var fieldRegistry = require('web.field_registry');
    var basicFields = require('web.basic_fields')
    var widgetRegistry = require('web.widget_registry');
    
    //Import des IoT Widget
    var iotWidget = require('iot.widgets');
    
    //Import de RPC pour les requêtes vers Python
    var rpc = require('web.rpc');
    
    //Affichage des logs
    console.log("Basic Field :");
    console.log(basicFields);
    console.log("Field Registry :");
    console.log(fieldRegistry);
    console.log("Widget Registry :");
    console.log(widgetRegistry);

    iotWidget.IoTRealTimeValue.include({
        
         _onValueChange: function (data){
            var self = this;
            console.log("RealTime :", data.value);
            this._setValue(data.value.toString())
                .then(function() {
                    if (!self.isDestroyed()) {
                        self._render();
                    }
                });
        },
    });
    iotWidget.IoTDeviceValueDisplay.include({
        
         _onValueChange: function (data){
            if (this.$el) {
                this.$el.text(data.value);
                console.log("Display :",data.value);
            }
        },
    });

    //Dans IoT widget il y a "IoTRealTimeValue" et c'est celui là qu'il faut extend/include avec une requête rpc pour pouvoir récupéré la valeur dans le modèle
    console.log("IotWidget :");
    console.log(iotWidget);
    
    
    
        
//     Phone.include({
//         events: _.extend({}, Phone.prototype.events, {
//             'click': '_onClick',
//         }),
//         _onClick: function (e) {
//             if (this.mode === 'readonly') {
//                 e.preventDefault();
//                 var phoneNumber = this.value;
//                 console.log(phoneNumber);
//                 console.log("Le numéro juste au dessus");
//                 // call the number on voip...
//             }
//         },
//     });
    
});