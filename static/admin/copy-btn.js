function copyToClip(e) {
    let val = e.getAttribute('value')
    console.log(val)
    navigator.clipboard.writeText(val);
  } 

// document.onreadystatechange = function () {
//     var myButton = '<div onClick="copyToClip(this)" value="ter" class="button">Copy</div>';
//     let $ = django.jQuery
//     $('.field-getTempLink').each(function( index ) {
//         // console.log( $( this ).text() );
//         // console.log( $( this )[0].innerHTML )
//         let uuid = $( this ).text()
//         if(uuid!=='-')
//             $( this )[0].outerHTML = '<div onClick="copyToClip(this)" value="kitchendotcom.in/custormerform/'+uuid+'" class="button">Copy</div>'
//         // console.log( $( this ).outerHTML )
//       });
// }