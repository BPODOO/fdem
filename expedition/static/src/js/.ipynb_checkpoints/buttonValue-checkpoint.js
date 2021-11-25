// function myFunction() {
//     console.log("Ici");
// }

odoo.define('my.component', function (require) {
    "use strict";

//     var FormController = require('web.FormController');
    
//       // create an anonymous function that we call immediately
//       // this will hold our previous focus variable, so we don't
//       // clutter the global scope
//     (function() {

//           // the variable to hold the previously focused element
//         var prevFocus;

//           // our single focus event handler
//         $("input").focus(function() {

//               // let's check if the previous focus has already been defined
//             if (typeof prevFocus  !== "undefined") {

//                   // we do something with the previously focused element
//                 $("#prev").html(prevFocus.val());
//             }

//               // AFTER we check upon the previously focused element
//               //   we (re)define the previously focused element
//               //   for use in the next focus event
//             prevFocus = $(this);
//             console.log(prevFocus);
//         });
//     })();
    
//     var formController = FormController.include({
//         _onButtonClicked: function (event) {
//             var y = document.activeElement.tagName;
//             console.log(y);
//             if(event.data.attrs.id === "button_js"){
//                 console.log("Dedans la fonction");
//                 var x = document.activeElement.tagName;
//                 console.log(x);
//             }
//         }
//     });
    
//     console.log("avant function");
//     $(document).ready(function() {
//          $('#button_id').click(function (e){
//              console.log("ici");
//              alert('Hello !!!');
//         });

//     });
});
