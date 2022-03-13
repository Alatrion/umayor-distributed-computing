const express = require('express');
const bodyParser = require('body-parser');
const responseTime = require('response-time');

const app = express();
app.use(bodyParser.urlencoded());
app.use(responseTime());
const port = process.env.PORT;
app.listen(port);

const delay = ms => new Promise(resolve => setTimeout(resolve, ms))

app.post('/sum-range', async function(req,res){
    console.log(req.body);
    let result = parseInt(0);
    var starting_number;
    var ending_number;
    starting_number = parseInt(req.body.starting_number);
    ending_number = parseInt(req.body.ending_number);
    for (let i = starting_number; i < ending_number; i++) {
        result = result + i;
        await delay(1000)
    }

    if (req.body.final === '1'){
        result = result + ending_number;
    }
    res.send(result.toString());
})

app.post('/sum', async function(req,res){
    console.log(req.body);
    let result = parseInt(0);
    var num1;
    var num2;
    num1 = parseInt(req.body.num1);
    num2 = parseInt(req.body.num2);
    result = num1 + num2;
    await delay(1000)
    res.send(result.toString());
})
