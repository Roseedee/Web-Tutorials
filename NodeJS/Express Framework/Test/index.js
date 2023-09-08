const express = require('express');
const path = require('path');

const app = express();

//route page
app.use(express.static(path.join(__dirname, 'views')))

//route api
app.use('/routes/api', require('./routes/api/user'))

const port = process.env.port || 5000;

app.listen(port, () => console.log(`server is running on port ${port}`));