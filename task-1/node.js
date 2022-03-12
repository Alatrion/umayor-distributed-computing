const { time } = require('console');
const express = require('express');

const app = express();

let result = 0;
app.post('/sum', function(req,res){
    let starting_number = req.body.starting_number;
    let ending_number = req.body.ending_number;
    for (let i = starting_number; i < ending_number; i++) {
        result = result + i;
        
    }
    res.send(result.toString());
})

// https://localhost:4000/sum?nums=1,2,3