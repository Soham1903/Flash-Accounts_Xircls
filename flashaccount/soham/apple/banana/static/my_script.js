console.log('version 9.5');

var formdata = new FormData();
formdata.append("shop", "sohamladgaonkar.myshopify.com");
var test
var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://0972-110-226-179-60.ngrok-free.app/valuetog/", requestOptions)
  .then(response => response.json())
  .then(result => 
    JSON.stringify(result.value))
  .then(jsonString => {
    
      
    test = jsonString
    console.log(test)
    if (test === "true" && (window.location.pathname.includes('/orders') || window.location.pathname.includes('/thank_you')))
{

  console.log(__st.cid)
  var cust_id = Shopify.checkout.customer_id
var myHeaders = new Headers();
myHeaders.append("X-Shopify-Access-Token", "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");
myHeaders.append("Content-Type", "application/json");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  redirect: 'follow'
};


let custom_activation = {activeUrl: ""}
fetch(`https://sohamladg.myshopify.com/admin/api/2022-04/customers/${cust_id}/account_activation_url.json`, requestOptions)
  .then(response => response.text())
  .then(result => {
    var select12 = document.querySelector("input[name=token]")
    select12.value = JSON.parse(result).account_activation_url.split(`/`).slice(-1)[0]
  })
  .catch(error => console.log('error', error));
  Shopify.Checkout.OrderStatus.addContentBox(`
   <div>
   <html>
   <head>
     <title>Sign In</title>
   </head>
   <body>

     <div style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
       <div style="max-width: 400px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 4px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
         <h2 style="text-align: center;">Sign In</h2>
        <form method="post" action="/account/activate" accept-charset="UTF-8">
  <input type="hidden" name="form_type" value="activate_customer_password">
  <input type="hidden" name="utf8" value="✓">
  <div class="field">
    <input type="password" name="customer[password]" id="password" autocomplete="new-password" placeholder="Password" style="width: 300px; padding: 10px; font-size: 16px;">
    <label for="password" style="display: block; margin-bottom: 5px;">
      Password
    </label>
  </div>
  <div class="field">
    <input type="password" name="customer[password_confirmation]" id="password_confirmation" autocomplete="new-password" placeholder="Confirm password" style="width: 300px; padding: 10px; font-size: 16px;">
    <label for="password_confirmation" style="display: block; margin-bottom: 5px;">
      Confirm password
    </label>
  </div>
  <button onclick = "myfunc()" style="padding: 10px 20px; font-size: 16px; background-color: #007bff; color: #fff; border: none; cursor: pointer;">
    Activate account
  </button>
  <button name="decline" style="padding: 10px 20px; font-size: 16px; background-color: #dc3545; color: #fff; border: none; cursor: pointer;">
    Decline invitation
  </button>
  <input type="hidden" name="token" value="">
  <input type="hidden" name="id" value="${cust_id}">
</form>

       </div>
     </div>
   </body>
   </html>
   </div>
`

  )

}


 
   
  })
  .catch(error => console.log('error', error));


// 