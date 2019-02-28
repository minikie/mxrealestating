var this_delimiters = ['[[',']]'];

var app = new Vue({
  el: '#message',
  data: {
    message : 'Hello Vue!'
  },
  delimiters: this_delimiters
})

var positionInfo_app = new Vue({
  el: '#positionInfo',
  data: {
    notional: undefined,
    book_value: undefined,
    effective_date: '2018-10-11'
  },
  delimiters: this_delimiters
})

var positionList_app = new Vue({
   el: '#positionList',
   data: {
    position_list: [],
   },
   delimiters: this_delimiters
});

var analysisResult_app = new Vue({
   el: '#analysisResult',
   data: {
    summary:{
        result_date:undefined,
        book_value: undefined,
        loan:{
            amount:0,
        },
        rent:{
            deposit:0
        },
        profit_percent: 0.03,
        profit_amount: 10000
    }
   },
   delimiters: this_delimiters
});


var storePositionInfo_app = new Vue({
  el: '#storePositionInfo',
  data: {
    email: 'minikie@naver.com',
    access_key: undefined
  },
  delimiters: this_delimiters
})

function positionInfo_validation() {
    tf = false;
    if (positionInfo_app.notional > 0)
    {
         tf = true;
    }

    return tf;
}

function addbtn_Click() {
    if (positionInfo_validation())
    {
        position = {
            notional: parseFloat(positionInfo_app.notional),
            book_value: parseFloat(positionInfo_app.notional)
            }
        positionList_app.position_list.push(position)
        console.log(positionList_app.position_list);
    }
    // list 에 더함
    // get list
}

function analysisbtn_Click() {
        axios.post('/analysis',{
        email: storePositionInfo_app.email,
        position_list: positionList_app.position_list
    })
        .then(function (response) {

        analysisResult_app.summary = response.data;

        console.log(response);
    }).catch(function (error) {
        console.log(error);
    });
}


function storePositionbtn_Click() {
    axios.post('/storepositions',{
        email: storePositionInfo_app.email,
        positions: positionList_app.position_list
    })
        .then(function (response) {
        storePositionInfo_app.access_key = response.data['access_key'];

        console.log(response);
    }).catch(function (error) {
        console.log(error);
    });
}

