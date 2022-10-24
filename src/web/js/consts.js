const localURL = "http://127.0.0.1:8000"


const formToJson = function (formId){
    var data = {};
    $("#"+formId).serializeArray().map( function(x) {
        data[x.name] = $('#'+x.name).val();
    });
    return data;
}

const jsonToForm = function (formId, json){
    $("#"+formId).serializeArray().map( function(x) {
        $('#'+x.name).val(json[x.name]);
    });
}