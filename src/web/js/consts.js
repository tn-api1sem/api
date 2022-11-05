const localURL = "http://127.0.0.1:8000"

const techLeader = 2;
const productOwner = 3;

const formToJson = function (formId){
    var data = {};
    $("#"+formId).serializeArray().map( function(x) {
        const el = $('#'+x.name).val();
        
        let isId = x.name.includes('id');
        let isArray = Array.isArray(el)
        
        if(isArray){
            for(let i = 0; i < el.length; i++){
                el[i] = parseInt(el[i]);
            }
        }
        
        data[x.name] =  isId ? (isArray ? el : parseInt(el)) : el.toString() ;
    });
    return data;
}

const jsonToForm = function (json){
    for (const [key, value] of Object.entries(json)) {
        if(Array.isArray(value)){
            $('#'+key)
            .val(value)
            .change();    
            continue;
        }
        
        $('#'+key).val(value);
    }
}