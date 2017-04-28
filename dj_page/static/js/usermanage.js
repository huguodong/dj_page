/**
 * Created by HELLO on 2017/4/21.
 */
$(function () {

    $("#all").click(function () {
        if (this.checked) {
            $("#tb :checkbox").prop("checked", true);
        } else {
            $("#tb :checkbox").prop("checked", false);
        }
    });
    $("#dedSelect").click(function () {
        arr = []
        $("input[name='id']:checkbox:checked").each(function () {
            arr.push($(this).val());
        })
        console.log(arr)
    });

});
function userCheck(ths) {
    if (ths.checked == false) {
        $("#all").attr('checked', false)
    }
}
function userdelete(id) {
    alert(id)
}
function userupdate(id) {
    alert(id)
}