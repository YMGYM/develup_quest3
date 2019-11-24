  $(document).ready(function () {
    $(".open").on('click', function () {
      $(".event_popup").show();
      $(".event_dim").show();
    });

    $(".event_close").on('click', function () {
      $(this).parent().hide();
      $(".event_dim").hide();
    });
  });

  function rowAdd() {
    var objRow;
    objRow = document.all["tableshow"].insertRow();

    var objCell_picture = objRow.insertCell();
    objCell_picture.innerHTML = "사진";

    var objCell_event = objRow.insertCell();
    objCell_event.innerHTML = "이벤트 명";

    var objCell_date = objRow.insertCell();
    objCell_date.innerHTML = "n일 남음 또는 n일 지남";

    var objCell_delete = objRow.insertCell();
    objCell_delete.outerHTML = "<td style='cursor:pointer;' onclick='javascript:delElement(this);'>X</td>";
  }

  function delElement(obj) {
    var index = obj.parentElement.rowIndex;
    document.getElementById('tableshow').deleteRow(index);
  }
