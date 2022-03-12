const express = require('express');
const bodyParser = require('body-parser');

const app = express();
//app.use(express.json());
app.use(bodyParser.urlencoded());
app.listen(3000);

app.post('/sum-range', function(req,res){
    console.log(req.body);
    let result = parseInt(0);
    var starting_number;
    var ending_number;
    starting_number = parseInt(req.body.starting_number);
    ending_number = parseInt(req.body.ending_number);
    for (let i = starting_number; i < ending_number; i++) {
        result = result + i;
    }
    if (req.body.final === '1'){
        result = result + ending_number;
    }
    res.send(result.toString());
})

app.post('/sum', function(req,res){
    let result = parseInt(0);
    var num1;
    var num2;
    num1 = parseInt(req.body.num1);
    num2 = parseInt(req.body.num2);
    result = num1 + num2;
    res.send(result.toString());
})



// https://localhost:4000/sum?nums=1,2,3