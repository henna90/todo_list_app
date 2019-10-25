const express = require('express')
const app = express()
const port = 8000

app.get('/',function (req, res) {
console.log("hit the server")
res.header("Access-Control-Allow-Origin", "*");
res.header("Access-Control-Allow-Headers", "X-Requested-With");
res.send('Hello World!')})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))