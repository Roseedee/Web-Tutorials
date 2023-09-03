const express = require('express')

const app = express()
//index page (localhost:8080/)
app.get('/', (req, res) => {
    res.send('<h1>Home page</h1>')
})

app.post('/', (req, res) => {
    res.send('Got a POST request')
})

app.put('/user', (req, res) => {
    res.send('Got a PUT request at /user')
})

app.delete('/user', (req, res) => {
    res.send('Got a DELETE request at /user')
})

app.listen(8080, function() {
    console.log('listen on port 8080')
})