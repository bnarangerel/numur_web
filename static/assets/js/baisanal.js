function myfunction2() {
  console.log(grecaptcha.getResponse());
  if (grecaptcha.getResponse() == "") {
    swal({
      title: "Амжилтгүй",
      text: "Captcha заавал бөглөнө үү!",
      icon: "warning",
      button: "Үргэжлүүлэх",
    });
  } else {
    var formData = {
      organization_name: $("#organization_name").val(),
      organization_webstite: $("#organization_webstite").val(),
      organization_employee: $("#organization_employee").val(),
      organization_type: $("#organization_type").val(),
      organization_social: $("#organization_social").val(),
      organization_property: $("#organization_property").val(),
      email: $("#email").val(),
      phone: $("#phone").val(),
      body: $("#body").val(),
      response: grecaptcha.getResponse(),
    };
  }
  $(document).ready(function () {
    $("form").submit(function (event) {
      $.ajax({
        type: "POST",
        url: "https://numur.mn/numurappbackend/rest/Backend/AdminWebService/web_set_corprate",
        data: formData,
        dataType: "json",
        success: function (data) {
          if (data["success"]) {
            swal({
              title: "Амжилттай",
              text: "Таньд амжилт хүсье!",
              icon: "success",
              button: "Болсон",
            });
          } else {
            swal({
              title: "Амжилтгүй",
              text: "Алдаа гарлаа дахин оролдно уу!",
              icon: "warning",
              button: "Үргэжлүүлэх",
            });
          }
        },
        encode: true,
      }).done(function (data) {
        console.log(data);
      });
      event.preventDefault();
    });
  });
}
