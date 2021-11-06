let value

//-----DELAY------------//
function delay(fn, ms) {
    let timer = 0
    return function(...args) {
      clearTimeout(timer)
      timer = setTimeout(fn.bind(this, ...args), ms || 0)
    }
  }
//----DELAY-------//


$(document).ready(function(){

    $('.check').on('click', function(e){
        CollectData()
    })

    $('#form-price_to').keyup(delay(function(){      
        CollectData()
        }, 500))
        
    $('#form-price_from').keyup(delay(function(){
        CollectData()
        }, 500))
            
})



function CollectData(){

    let data = {}
        $('.check').each(function(){
            if($(this).is(':checked')){
                if(data.hasOwnProperty($(this).attr('name'))){
                    value = data[$(this).attr('name')]
                    value.push($(this).val())
                    data[$(this).attr('name')] = value
                }
                else{
                    data[$(this).attr('name')] = [$(this).val()]
                }

            }
        })
    data['form-price_to'] = $('#form-price_to').val()
    data['form-price_from'] = $('#form-price_from').val()
    data['url-par1'] = $('#filter-form').attr('data-typeone')
    data['url-par2'] = $('#filter-form').attr('data-typetwo')
    AJAX_FILTER(data)

}


function AJAX_FILTER(data){
    $.ajax({
        url: '/catalog/filter/',
        data: data,
        method: 'GET',
        dataType: 'json',


        success: function(res_filter){
            $('.right-catalog').html(res_filter.render);
            RELOAD_ELEM();
        }

    })

}